from django.contrib import admin
from volunteers.models import Volunteer



# Register your models here.


from .models import *

admin.site.register(Volunteer)
