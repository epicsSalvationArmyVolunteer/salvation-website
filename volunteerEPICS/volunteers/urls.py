from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.signin, name='sign-in'), #links to /volunteers/sign-in
    path('sign-up/', views.signup, name='sign-up'), #links to /volunteers/sign-up
    path('sign-out/', views.signout, name='sign-out'), #links to /volunteers/sign-out
    path('thanks/', views.thanks, name='thanks'),  #links to /volunteers/thanks
    path('', views.volunteers, name='volunteershome'), #links to /volunteers (as indecaded by the '')
    path('create/', views.create, name='create'), #test simple form for Mikayla

]
