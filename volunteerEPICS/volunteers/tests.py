from django.test import TestCase
from django.contrib.auth.models import User
from volunteers.models import Event, Volunteer

# Create your tests here.

class VolunteerModelTests(TestCase):
    """
    Test that the 'last_event' method on user is working properly
    """

    def test_last_event(self):
        """
        the last event the volunteer attended is the most recent event
        """
        user = User.objects.create_user(username='testuser', password='1234')

        event1 = Event.objects.create(name='testevent1', date='1990-07-03', length=2)
        event2 = Event.objects.create(name='testevent2', date='2002-07-03', length=3.5)

        event1.volunteers.add(user.volunteer)
        event2.volunteers.add(user.volunteer)


        last = user.volunteer.last_event()
        self.assertIs(last, event2)
