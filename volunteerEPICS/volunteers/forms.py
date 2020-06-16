from django.forms import ModelForm
from .models import Volunteer
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField



#I (James) am modifying this based off of what I see here:
#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-profile-model
class VolunteerCreationForm(UserCreationForm):
  """Form to create new volunteers"""
  phone = PhoneNumberField()
  emergency_contact_name = forms.CharField()
  emergency_contact_phone = PhoneNumberField()
  employer_name = forms.CharField()
  gender = forms.CharField()
  birth_date = forms.DateField()
  state_zip = forms.CharField()
  comment = forms.CharField(required=False)

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')


#<h1>Sign out Page used for testing</h1>
#<form action"" method="post">
 # {% csrf_token %}
  #{{form.First_name.label}}
  #{{form.First_name}}


  #<input type ="submit">

    #</form>
