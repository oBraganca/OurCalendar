from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django import forms

from users.models import CustomUser

import random
import string
import datetime


class OurCalendar(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    qnt_merge = models.IntegerField()

    def __str__(self):
        return "Calendar_%s" % self.id


def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    

def unique_id_generator(instance):
    new_id = random_string_generator()
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(unic_code = new_id).exists()
    if qs_exists:
        return unique_id_generator(instance)
    return new_id


def pre_save_create_id(sender, instance, *args, **kwargs):
    if not instance.unic_code:
        instance.unic_code = unique_id_generator(instance)



ACCESS = (
    ('PB', 'Public'),
    ('PV', 'Private')
)

class Events(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    visible = models.BooleanField(default=True)
    calendar = models.ForeignKey(OurCalendar, on_delete=models.CASCADE)
    origim = models.ForeignKey(OurCalendar,  on_delete=models.CASCADE, related_name="+")
    unic_code = models.CharField(max_length=255, blank=True)
    access = models.CharField(max_length=255, choices=ACCESS, blank=False, null=False)

    def __str__(self):
        return self.name
    

class RequestCalendarFollow(models.Model):
    calendar = models.ForeignKey(OurCalendar, on_delete=models.CASCADE)
    follower =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.follower)
    
class CalendarFollow(models.Model):
    calendar = models.ForeignKey(OurCalendar, on_delete=models.CASCADE)
    follower =  models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="follower")
    qnt_merge = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.follower)


pre_save.connect(pre_save_create_id, sender = Events)