from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .forms import VolunteerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
# Create your views here.


def signin(request):  #signin page defenition
    return render(request,'volunteers/signin.html' ) #sends Django to templates for signin.html

def signout(request):  #signup page defenition
        return render(request,'volunteers/signout.html' )

def thanks(request):   #thank you page defenition
    return render(request,'volunteers/thanks.html' )

def signup(request):  #sign out page defenition
    form=VolunteerForm()

    if request.method=='POST':
        print(request.POST)
        form=VolunteerForm(request.POST) #instance=profile)
        if form.is_valid():
            form.save()
    context={'form':form}

    return render(request,'volunteers/signup.html', context )  #this will look at the templeate subdirecorty and find the .html file

def volunteers(request): #defenition for just /volunteers
    return render(request,'volunteers/volunteershome.html' )




def create(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']

        user = User.objects.create_user(username=username, email=email,first_name=first_name, last_name=last_name)
        user.save();
        print('user created!')
        return redirect('/')
    else:
        return render (request, 'volunteers/testing.html' )
