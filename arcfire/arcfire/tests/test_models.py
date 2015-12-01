from .TestUtils import TestUtils
from arcfire.models import *


class ModelTestCase(TestUtils):
    '''
    This is to test whether models behave, and have correct properties.
    '''
    def setUp(self):
        Event.objects.create(name="World War II", slug="world-war-ii")
        Event.objects.create(name="War of 1812", slug="war-1812")

    def test_events_exist(self):
        '''
        Events exist.
        '''
        events = Event.objects.all()
        self.assertEqual(events.count(), 2)
