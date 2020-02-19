from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def signin(request):  #signin page defenition
    return render(request, 'volunteers/signin.html' ) #sends Django to templates for signin.html

def signup(request):  #signup page defenition
    return HttpResponse('<h1>sign up page</h1>')

def thanks(request):   #thank you page defenition
    return HttpResponse('<h1>Thank you for volunteering (making magic!)</h1>')

def signout(request):
    return HttpResponse('<h1>sign out page hi ivana</h1>')  #sign out page defenition

def volunteers(request):
    return HttpResponse('<h1>home page for volunteers</h1>')  #defenition for just /volunteers
