from django.test import TestCase, Client
import factory
from pyquery import PyQuery as pq
from arcfire.models import (
    Picture,
    Plan,
    Keyword,
    Property,
    Item,
    Event,
    Person,
    Place,
    Collection,
    Group,
    Location,
    Relation
)


class ModelTestCase(TestCase):
    '''
    This is mostly a test of the tests at the moment.
    TODO: expand to test other models.
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


class TemplateTestCase(TestCase):
    ''''''
    def setUp(self):
        pass

    def html_subset(input_string, css_selector):
        return 'flurg'

    def test_get_response(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

        content = response.content.decode('utf-8')

        d = pq(content)
        print(type(d("#page_title")))
