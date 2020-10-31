# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.core.files.storage import FileSystemStorage


#fs = FileSystemStorage(location='/media/photos')

# Create your models here.
class Profile(models.Model):
    RESIDENT = 1
    ADMINISTRATOR = 2
    ROLE_CHOICES = (
        (RESIDENT, 'Resident'),
        (ADMINISTRATOR, 'Administrator'),
    )
    name = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True, default='static/images/default.png')
    age = models.IntegerField(null=True)
    contact = models.IntegerField(null=False, max_length=30)
    address = models.CharField(max_length=250)
    estate = models.ForeignKey('Neighbourhood', on_delete=models.CASCADE, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'profile'
        ordering = ['name']

    def __str__(self):  # __unicode__ for Python 3
        return f'{self.name}'

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(name=instance)
        instance.profile.save()

class Neighbourhood(models.Model):
    name = models.CharField(max_lenth=100)
    location = models.CharField(max_length=150)
    image = models.ImageField(upload_to='hood_images/', blank=True, max_length=None)

    class Meta:
        db_table = 'neighbourhoods'
        ordering = ['name']
