# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.contrib import messages

from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from common.classes.DBManager import DBManager
from common.middleware import RequestMiddleware

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
)

DATE_CHOICES = [(i,i) for i in range(1,32)]

MONTH_CHOICES = (
    (1, 'January'),(2, 'February'),(3, 'March'),(4, 'April'),(5, 'May'),(6, 'June'),(7, 'July'),
    (8, 'August'), (9, 'September'),(10, 'October'), (11, 'November'),(12, 'December')
)

YEAR_CHOICES = [(i,i) for i in range(1930,2006)]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    town = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    blocked = models.BooleanField(blank=True, null=True, default=0)




'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        create_user_profile(instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):

    if hasattr(instance, 'profile'):
        instance.profile.save()
    else:
        create_user_profile(instance)


def create_user_profile(instance):

    default_country = 1
    default_inviter = 3

    gender = 2
    date_of_birth = None
    country = None
    inviter = None
    address = None
    phone = None
    town = None
    location = None

    if hasattr(instance, 'country'):
        country = Country.objects.filter(id = default_country).first()

    if hasattr(instance, 'inviter'):
        inviter = User.objects.filter(id = default_inviter).first()

    if hasattr(instance, 'location'):
        location = instance.location

    if hasattr(instance, 'address'):
        address = instance.address

    if hasattr(instance, 'phone'):
        phone = instance.phone
        
    if hasattr(instance, 'town'):
        town = instance.location

    Profile.objects.create(
        user=instance,
        gender=gender,
        date_of_birth = date_of_birth,
        country = country,
        inviter = inviter,
        address = address,
        phone = phone,
        town = town,
        location = location
    )
'''