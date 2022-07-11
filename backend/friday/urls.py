from django.urls import path
from . import views

app_name='friday'

urlpatterns =[
    path('home/<int:temprature>/<int:humidity>/<int:pir>/<int:ldr>/<str:password>/', views.home_recived_data, name='home_recived_data'),
    path('home/live/', views.Live.as_view(), name='live' ),
    path('api/', views.api, name='api' ),
    path('lamp/on/', views.lamp_on, name='lamp_on'),
    path('lamp/off/', views.lamp_off, name='lamp_off'),
    path('relay/on/', views.relay_on, name='relay_on'),
    path('relay/off/', views.relay_off, name='relay_off'),
    path('control/', views.friday_control, name='control'),
]