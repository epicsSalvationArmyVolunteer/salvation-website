from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import VolunteerCreationForm
from .models import Volunteer
from django.contrib.auth import login, authenticate
# Create your views here.


def signin(request):  #signin page defenition
    return render(request, 'volunteers/signin.html' ) #sends Django to templates for signin.html

def signout(request):  #signup page defenition
        return render(request,'volunteers/signout.html' )

def thanks(request):   #thank you page defenition
    return render(request,'volunteers/thanks.html' )


def volunteers(request): #defenition for just /volunteers
    return render(request, 'volunteers/volunteershome.html' )

def signUp(request):
    """Registers new users, logs them in, and handles addtional comments"""
    if request.method == 'POST':
        print(request.POST)
        volunteer_form = VolunteerCreationForm(request.POST)
        if volunteer_form.is_valid():
            user = volunteer_form.save()
            user.refresh_from_db() # loads the volunteer instance created by the signal
            
            # populate volunteer with extra information from form
            user.volunteer.phone = volunteer_form.cleaned_data.get('phone')
            user.volunteer.emergency_contact_name = volunteer_form.cleaned_data.get('emergency_contact_name')
            user.volunteer.emergency_contact_phone = volunteer_form.cleaned_data.get('emergency_contact_phone')
            user.volunteer.employer_name = volunteer_form.cleaned_data.get('employer_name')
            user.volunteer.gender = volunteer_form.cleaned_data.get('gender')
            user.volunteer.birth_date = volunteer_form.cleaned_data.get('birth_date')
            user.volunteer.state_zip = volunteer_form.cleaned_data.get('state_zip')
            
            # If a comment is included, it should be saved seperately, and probably sent as an email to someone. How do we do this?

            # log user in and redirect to volunteer homepage
            username = volunteer_form.cleaned_data.get('username')
            raw_password = volunteer_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/volunteers')
    
    else:
        volunteer_form = VolunteerCreationForm()
    
    context = {'form':volunteer_form}
    return render(request, 'volunteers/signup.html', context)


