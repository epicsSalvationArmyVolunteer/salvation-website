from django.contrib import admin
from volunteers.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    """Controls Event form on Admin page"""
    exclude = ('volunteers',)

admin.site.register(Event, EventAdmin)
