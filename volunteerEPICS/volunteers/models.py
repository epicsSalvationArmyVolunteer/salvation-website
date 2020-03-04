"""models that are used in the volunteer tracking application"""
import datetime
from django.db import models
from  django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Volunteer(models.Model):
    """Volunteer is a 'Profile' that allows a user to be linked to events"""
    #Using a OneToOne field to link a user to a Volunteer
    #See https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Phone number field - see
    #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone = PhoneNumberField()

    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone = PhoneNumberField()

    employer_name = models.CharField(max_length=200)

    #Add gender choice field
    gender=models.CharField(default='null', max_length=100)

    birth_date = models.DateField(verbose_name='date of birth')

    #We only want to store state and zip
    state_zip = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username

    def last_event(self):
        """Last event the volunteer attended"""
        return self.events.latest('date')

    def events_since(self, since=models.DateTimeField):
        """all events the volunteer has attended between since and now"""
        return self.events.filter(date__gte=since, date__lte=datetime.datetime.now())


#See https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
#for reciever code
@receiver(post_save, sender=User)
def create_user_volunteer(sender, instance, created, **kwargs):
    """automatically creates a volunteer after a user is created"""
    if created:
        Volunteer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_volunteer(sender, instance, **kwargs):
    """automatically saves volunteer after user is saved"""
    instance.volunteer.save()


class Event(models.Model):
    """Event model"""
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date of event')
    max_volunteers = models.IntegerField('maximum number of volunteers', default=0)
    length = models.FloatField('duration (in hours) of event')

    #Link volunteers to events with a Many to Many field.
    #See https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ManyToManyField
    volunteers = models.ManyToManyField(Volunteer, related_name='events')

    def __str__(self):
        return self.name

    def volunteers_at_event(self):
        """Returns a query set of all volunteers at event"""
        return self.volunteers
