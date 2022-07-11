from django.urls import path
from . import views

app_name='friday'

urlpatterns =[
    #the sensores values are sent by nodemcu in this way
    path('home/<int:temprature>/<int:humidity>/<int:pir>/<int:ldr>/<str:password>/', views.home_recived_data, name='home_recived_data'),

    #live values are displayed in this url
    path('home/live/', views.Live.as_view(), name='live' ),

    #nodemcu will check this url for status
    path('api/', views.api, name='api' ),

    #these 4 urls are for turing relay on or off
    #region relay
    path('lamp/on/', views.lamp_on, name='lamp_on'),
    path('lamp/off/', views.lamp_off, name='lamp_off'),
    path('relay/on/', views.relay_on, name='relay_on'),
    path('relay/off/', views.relay_off, name='relay_off'),
    #endregion

    #control part of the app will be availabe in this url
    path('control/', views.friday_control, name='control'),
]