from django.test import TestCase, Client
import factory
from .TestUtils import TestUtils
from django.core.urlresolvers import reverse
from arcfire.models import (
    Collection,
    Event,
    Group,
    Keyword,
    Location,
    Person,
    Picture,
    Place,
    Plan,
    Property,
    Relation,
    Thing,
)


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


class TemplateTestCase(TestUtils):
    '''
    Basic tests to ensure templates are in order, and urls are accessible.
    '''
    def setUp(self):
        self.c = Client()
        # Collection.objects.create(name="Gum Wall", slug="gum-wall")
        Event.objects.create(name="War of 1812", slug="war-1812")
        # Group.objects.create(name="Democratic Party", slug="democratic-party")
        Keyword.objects.create(name="Wars", slug="wars")
        Person.objects.create(name="Napoleon", slug="napoleon")
        Picture.objects.create(
            name="Demoiselles d'Avignon", slug="demoiselles")
        Place.objects.create(name="North Pole", slug="north-pole")
        Plan.objects.create(name="Elevation", slug="elevation")
        Property.objects.create(name="Brown Hair", slug="brown-hair")
        Thing.objects.create(name="Curling Iron", slug="curling-iron")


    def test_home(self):
        '''Home page should load.'''
        response_1 = self.c.get('/')
        response_2 = self.c.get(reverse('home'))

        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_1.content, response_2.content)

        content = response_1.content.decode('utf-8')
        self.assert_in_html(
            content, '#page_title', ['Welcome to Arcfire.'], ['Flurble.'])

    def test_urls(self):
        '''Primary urls should load.'''
        responses = []
        # responses.append(self.c.get(reverse('collection_list'))) # TODO 
        responses.append(self.c.get(reverse('event_list')))
        # responses.append(self.c.get(reverse('group_list'))) # TODO 
        responses.append(self.c.get(reverse('keyword_list')))
        responses.append(self.c.get(reverse('location_list')))
        responses.append(self.c.get(reverse('person_list')))
        responses.append(self.c.get(reverse('picture_list')))
        responses.append(self.c.get(reverse('place_list')))
        responses.append(self.c.get(reverse('plan_list')))
        responses.append(self.c.get(reverse('property_list')))
        responses.append(self.c.get(reverse('relation_list')))
        responses.append(self.c.get(reverse('thing_list')))
        # responses.append(self.c.get(
        #     reverse('collection', args=['gum-wall']))) # TODO
        # responses.append(self.c.get(
        #     reverse('group', args=['democratic-party']))) # TODO
        responses.append(self.c.get(reverse('event', args=['war-1812'])))
        responses.append(self.c.get(reverse('keyword', args=['wars'])))
        responses.append(self.c.get(reverse('person', args=['napoleon'])))
        responses.append(self.c.get(reverse('picture', args=['demoiselles'])))
        responses.append(self.c.get(reverse('place', args=['north-pole'])))
        responses.append(self.c.get(reverse('plan', args=['elevation'])))
        responses.append(self.c.get(reverse('property', args=['brown-hair'])))
        responses.append(self.c.get(reverse('thing', args=['curling-iron'])))
        # responses.append(self.c.get(reverse('location', args=[]))) # TODO 

        for r in responses:
            # check that each url works
            self.assertEqual(r.status_code, 200)

            # decode and make sure each has basic elements
            content = r.content.decode('utf-8')
            self.assert_in_html(content, 'nav > div#nav_container > h3',
                ['Navigation'], ['Flurble.'])


