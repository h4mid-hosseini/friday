from datetime import date
from django.utils import timezone
from django.db import models

#this part of models defines important varibales to save sensoers value and adds time to it
class HomeSide(models.Model):
    #tempratue and humidity varibales will be filled by DHT11 
    tempratue       =           models.IntegerField         (verbose_name='دمای خانه', null=True, blank=True)
    humidity        =           models.IntegerField         (verbose_name='رطوبت', null=True, blank=True)
    #pir module output is a 0-1 number which can be used as boolean
    pir             =           models.BooleanField         (verbose_name='وضعیت سنسور حرکت',blank=True, null=True)
    #ldr number is somthing between 0 and 1023 whcih comes from analog pin of nodemcu
    ldr             =           models.IntegerField         (verbose_name='میزان نور', blank=True, null=True)
    #django will fill this field every time new values are recived
    date            =           models.DateTimeField        (auto_now=True, verbose_name='تاریخ')


    def __str__(self):
        return str(self.date)


class ServerSide(models.Model):
    #this variable will be used to control lamp or the relay connected to nodemcu
    lamp            =           models.BooleanField         (verbose_name='لامپ', null=True, blank=True)
    #the below variable will show the second relay status
    relay2          =           models.BooleanField         (verbose_name='رله شماره دو', null=True, blank=True)
    #date will be added automaticly when ever new instans are build
    date            =           models.DateTimeField        (auto_now=True, verbose_name='تاریخ')
    # if this variable set to True, after detecting any movemnet by PIR, relay2 will be set to True and someting you define will turn on!
    alert_mode      =           models.BooleanField         (verbose_name='حالت هشدار دهی', blank=True, null=True)
    

    def __str__(self):
        return str(self.date)