from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import HomeSide, ServerSide
from django.views.generic import ListView


#this variable will be used to athenticate the values
#there is 'password' varibale in nodemcu code for the porpuse, they should be the same
server_password = 'yourpassword'


#this function recives and saves the sensors value
def home_recived_data(request, temprature, humidity, pir, ldr, password):
    #here is the password are compared
    if password==server_password:
        #if password is matched, new object will be created to store new values
        home = HomeSide.objects.create(tempratue=temprature,humidity=humidity, pir=pir, ldr=ldr)
        
        #the last status of relaies in our database is got
        obj = ServerSide.objects.last()
        #if value of home pir and alert mode are both set to True, the below relay will become True
        if home.pir and obj.alert_mode:
            obj.relay2 = True
            obj.save()
        home.save()
        return HttpResponse(status=200)
    else:
        #here is the case of not matching passwords
        return HttpResponse('پسورد نا معتبر')


#all saved sensors value will be shown by this CBV and will be paginated by 200 per page
class Live(ListView):
      model = HomeSide
      paginate_by = 200
      context_object_name = 'results'
      template_name = 'friday.html'
      #results will be sorted by the latest
      ordering = ['-date']


#here is where relaies status are outputed for nodemcu to get
def api(request):
    obj = ServerSide.objects.last()
    lamp = obj.lamp
    relay= obj.relay2
    return JsonResponse({'lamp':lamp, 'relay':relay})


#the 4 below functions are for controling relaies
#region controling
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
#endregion


#this function is used to show controling page
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