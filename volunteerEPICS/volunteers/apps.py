from django.apps import AppConfig
#from volunteerEPICS.volunteers.models import Volunteer


class VolunteersConfig(AppConfig):
    name = 'volunteers'


def volunteer_login(volunteer, event):
    """Call this function to "login" a volunteer to an event"""
    event.add(volunteer)


def volunteer_hours(volunteer, number_of_events):
    """Return the number of hours in the events in the specified range"""
    """The range is an integer greater than one, and refers to events from most to least recent"""
    if number_of_events <= 0:
        return "Bad range, range must be a positive integer"
    return volunteer.events.all.filter()


def all_employees_of_company(company):
    """
    Return all volunteers whose employer is company
    """
    return Volunteer.objects.filter(employer=company)
