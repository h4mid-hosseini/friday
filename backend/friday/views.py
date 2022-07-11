from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import HomeSide, ServerSide
from django.views.generic import ListView


password = 'yourpassword'


def home_recived_data(request, temprature, humidity, pir, ldr, password):
    home = HomeSide.objects.create(tempratue=temprature,humidity=humidity, pir=pir, ldr=ldr)
    obj = ServerSide.objects.last()
    if home.pir and obj.alert_mode:
        obj.relay2 = True
        obj.save()
    home.save()
    return HttpResponse(status=200)


class Live(ListView):
      model = HomeSide
      paginate_by = 200
      context_object_name = 'results'
      template_name = 'friday.html'
      ordering = ['-date']

def api(request):
    obj = ServerSide.objects.last()
    lamp = obj.lamp
    relay= obj.relay2
    return JsonResponse({'lamp':lamp, 'relay':relay})


def lamp_on(request):
    if request.user.is_superuser:
        obj = ServerSide.objects.last()
        obj.lamp = True
        obj.save()
        return redirect('friday:control')
    else:
        raise Http404("Not Allowed!")

def lamp_off(request):
    if request.user.is_superuser:
        obj = ServerSide.objects.last()
        obj.lamp = False
        obj.save()
        return redirect('friday:control')
    else:
        raise Http404("Not Awllowed!")


def relay_on(request):
    if request.user.is_superuser:
        obj = ServerSide.objects.last()
        obj.relay2 = True
        obj.save()
        return redirect('friday:control')
    else:
        raise Http404("Not Allowed!")


def relay_off(request):
    if request.user.is_superuser:
        obj = ServerSide.objects.last()
        obj.relay2 = False
        obj.save()
        return redirect('friday:control')
    else:
        Http404("Not Allowed!")


def friday_control(request):
    if request.user.is_superuser:
        obj = ServerSide.objects.last()
        lamp_status = obj.lamp
        relay_status =obj.relay2
        context={
            'lamp_status':lamp_status,
            'relay_status':relay_status,
        }
        return render(request, 'friday-control.html', context)
    
    else:
        raise Http404("Not Allowed!")