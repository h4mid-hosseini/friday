from django.contrib import admin
from .models import HomeSide, ServerSide
# Register your models here.

class HomeAdmin(admin.ModelAdmin):
    list_display = ['tempratue', 'humidity', 'pir', 'ldr', 'date']
    list_filter = ['date', 'pir']


class ServerAdmin(admin.ModelAdmin):
    list_display = ['lamp', 'relay2', 'date']
    
admin.site.register(HomeSide, HomeAdmin)
admin.site.register(ServerSide, ServerAdmin)