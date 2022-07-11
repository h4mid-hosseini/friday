from django.contrib import admin
from .models import HomeSide, ServerSide

#this class defines how sensors data are displayed in django admin panel
class HomeAdmin(admin.ModelAdmin):
    list_display = ['tempratue', 'humidity', 'pir', 'ldr', 'date']
    list_filter = ['date', 'pir']

#this class defines how relay statuses are displayed in django admin panel
class ServerAdmin(admin.ModelAdmin):
    list_display = ['lamp', 'relay2', 'date']
    
admin.site.register(HomeSide, HomeAdmin)
admin.site.register(ServerSide, ServerAdmin)