from django.test import TestCase, Client
from django.contrib.auth.models import User
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
        # Group.objects.create(
           # name="Democratic Party", slug="democratic-party")
        Keyword.objects.create(name="Wars", slug="wars")
        Person.objects.create(name="Napoleon", slug="napoleon")
        Picture.objects.create(
            name="Demoiselles d'Avignon", slug="demoiselles")
        Place.objects.create(name="North Pole", slug="north-pole")
        Plan.objects.create(name="Elevation", slug="elevation")
        Property.objects.create(name="Brown Hair", slug="brown-hair")
        Thing.objects.create(name="Curling Iron", slug="curling-iron")

    def test_home(self):
        '''
        Home page should load.
        '''
        response_1 = self.c.get('/')
        response_2 = self.c.get(reverse('home'))

        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_1.content, response_2.content)

        content = response_1.content.decode('utf-8')
        self.assert_in_html(
            content, '#page_title', ['Welcome to Arcfire.'], ['Flurble.'])

    def test_urls(self):
        '''
        Primary urls should load.
        '''
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
        responses.append(self.c.get(reverse('login')))
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


class UserTestCase(TestUtils):
    '''
    Tests covering users, auth, and other account-type stuff.
    '''

    def setUp(self):
        self.c = Client()
        self.duke = User.objects.create_user(
            username='wellington', password='waterloo')
        self.assertEqual(User.objects.all().count(), 1)

    def test_login(self):
        '''
        User should be able to login using custom form, and should receive a
        successful message.
        '''
        # make sure nobody's logged in
        self.assertEqual(self.c.session.get('_auth_user_id'), None)

        # Pre-login
        login_page = self.c.get(reverse('login'))
        self.assertEqual(login_page.status_code, 200)
        content = login_page.content.decode('utf-8')
        self.assert_in_html(content, '#page_title', ['Login to Arcfire.'])
        self.assert_in_html(content, 'nav > div#nav_container',
                ['Login'], ['Logout'])

        # Login
        response = self.c.post(reverse('login'),
            {'username': 'wellington', 'password': 'waterloo'}, follow=True,)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(
            int(self.c.session.get('_auth_user_id')),self.duke.pk)

        # Make sure resulting page is right: correct message, nav changes
        content = response.content.decode('utf-8')
        self.assert_in_html(content, '#messages', ['Login successful.'])
        self.assert_in_html(content, '#nav_absolute', ['Logout'], ['Login'])

    def test_logout(self):
        '''
        User should be able to logout.
        '''
        # Login
        response = self.c.post(reverse('login'),
            {'username': 'wellington', 'password': 'waterloo'})
        self.assertEqual(
            int(self.c.session.get('_auth_user_id')), self.duke.pk)

        # Logout
        self.c.get(reverse('logout'))
        self.assertEqual(self.c.session.get('_auth_user_id'), None)