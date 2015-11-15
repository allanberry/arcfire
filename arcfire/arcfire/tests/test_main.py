from django.test import TestCase
import factory
from arcfire.models import Picture, Plan, Keyword, Property, Item, Event, Person, Place, Collection, Group, Location, Relation



class EventTestCase(TestCase):
    def setUp(self):
        event_1 = Event.objects.create(name="World War II", slug="world-war-ii")
        event_2 = Event.objects.create(name="War of 1812", slug="war-1812")

    def test_events_exist(self):
        '''
        Events exist.
        '''
        events = Event.objects.all()
        self.assertEqual(events.count(), 2)