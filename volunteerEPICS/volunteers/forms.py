from django.forms import ModelForm
from .models import Volunteer
from django import forms


class VolunteerForm(ModelForm):
    class Meta:
        model = Volunteer
        #comment = forms.CharField(widget=forms.Textarea)

#fields to include on the form excluding user because idk if we need them to see that
        fields= ['comment','event_volunteering','username','First_name','Last_name','gender','phone','email','emergency_contact_name','emergency_contact_phone','employer_name', 'birth_date', 'state', 'state_zip']





#<h1>Sign out Page used for testing</h1>
#<form action"" method="post">
 # {% csrf_token %}
  #{{form.First_name.label}}
  #{{form.First_name}}


  #<input type ="submit">

    #</form>
