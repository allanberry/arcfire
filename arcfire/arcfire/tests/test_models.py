from django.test import TestCase
from arcfire.models import *

# it doesn't make much sense to fill this out until I have factories working correctly.


class RelationTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class LocationTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class KeywordTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class PropertyTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class PictureTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class PlanTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class ItemTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class EventTestCase(TestCase):
    '''
    Events.
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


class ThingTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class PlaceTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class PersonTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class CollectionTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass


class GroupTestCase(TestCase):
    '''
    Relations.
    '''

    def setUp(self):
        pass