"""models that are used in the volunteer tracking application"""
import datetime
from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
#from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Volunteer(models.Model):
    """Volunteer is a 'Profile' that allows a user to be linked to events"""
    #Using a OneToOne field to link a user to a Volunteer
    #See https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Phone number field - see
    #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    #phone = PhoneNumberField()
    username = models.CharField(default='null',max_length=200)
    First_name = models.CharField(default='null',max_length=200)
    Last_name = models.CharField(default='null',max_length=200)
    email = models.CharField(default='null',max_length=200)
    employer_name = models.CharField(default='null',max_length=200)
    emergency_contact_name = models.CharField(default='null', max_length=200)
    emergency_contact_phone = models.CharField(default='null', max_length=200)
    phone = models.CharField(default='null', max_length=200)
    event_volunteering = models.CharField(default='null', max_length=500)
    comment = models.CharField(default='null', max_length=500)  # need to figure out for to make this bigger, possibly with widgets but need more time to mess around with this. 

    #emergency_contact_phone = PhoneNumberField()


    employer_name = models.CharField(default='null',max_length=200)


    #TODO Add gender choice field
    gender = models.CharField(default='null', max_length=100)

    birth_date = models.DateField(default = 'mm/dd/yyyy',verbose_name='date of birth')

    #Don't care about address, only state and zip.
    state = models.CharField(default = 'null',max_length=500)
    state_zip = models.CharField(default = 'null',max_length=500)

    def __str__(self):
        return self.user.username

    def last_event(self):
        """Last event the volunteer attended"""
        return self.events.latest('date')

    def events_since(self, since=models.DateTimeField):
        """all events the volunteer has attended between since and now"""
        return self.events.filter(date__gte=since, date__lte=datetime.datetime.now())

    def hours_since(self, since=models.DateTimeField):
        """the total number of hours the volunteer has worked between since and now"""
        events = self.events_since(since)
        return events.sum('length')
