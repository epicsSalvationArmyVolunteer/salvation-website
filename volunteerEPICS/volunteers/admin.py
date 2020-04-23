from django.contrib import admin
from volunteers.models import Event, Volunteer

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    """Controls Event form on Admin page"""
    exclude = ('volunteers',)

admin.site.register(Event, EventAdmin)

admin.site.register(Volunteer)