from datetime import date
from django.utils import timezone
from django.db import models

# Create your models here.
class HomeSide(models.Model):
    tempratue       =           models.IntegerField         (verbose_name='دمای خانه', null=True, blank=True)
    humidity        =           models.IntegerField         (verbose_name='رطوبت', null=True, blank=True)
    pir             =           models.BooleanField         (verbose_name='وضعیت سنسور حرکت',blank=True, null=True)
    ldr             =           models.IntegerField         (verbose_name='میزان نور', blank=True, null=True)
    date            =           models.DateTimeField        (auto_now=True, verbose_name='تاریخ')

    def __str__(self):
        return str(self.date)

class ServerSide(models.Model):
    lamp            =           models.BooleanField         (verbose_name='لامپ', null=True, blank=True)
    relay2          =           models.BooleanField         (verbose_name='رله شماره دو', null=True, blank=True)
    date            =           models.DateTimeField        (auto_now=True, verbose_name='تاریخ')
    alert_mode      =           models.BooleanField         (verbose_name='حالت هشدار دهی', blank=True, null=True)
    

    def __str__(self):
        return str(self.date)