from django.test import TestCase, Client
from django.contrib.auth.models import User
import factory
from .TestUtils import TestUtils
from django.core.urlresolvers import reverse
from arcfire.models import *
from arcfire.views import *


class TemplateGlobalTestCase(TestUtils):
    '''
    Basic tests to ensure templates are in order, and urls are accessible.
    '''
    def setUp(self):
        c = Client()
        Event.objects.create(name="War of 1812", slug="war-1812")
        Keyword.objects.create(name="Wars", slug="wars")
        Person.objects.create(name="Napoleon", slug="napoleon")
        Picture.objects.create(
            name="Demoiselles d'Avignon", slug="demoiselles")
        Place.objects.create(name="North Pole", slug="north-pole")
        Plan.objects.create(name="Elevation", slug="elevation")
        Property.objects.create(name="Brown Hair", slug="brown-hair")
        Thing.objects.create(name="Curling Iron", slug="curling-iron")

        # some canned responses

        responses = []
        responses.append(c.get(reverse('home')))
        responses.append(c.get(reverse('login')))

        responses.append(c.get(reverse('event_list')))
        responses.append(c.get(reverse('keyword_list')))
        responses.append(c.get(reverse('person_list')))
        responses.append(c.get(reverse('picture_list')))
        responses.append(c.get(reverse('place_list')))
        responses.append(c.get(reverse('plan_list')))
        responses.append(c.get(reverse('property_list')))
        responses.append(c.get(reverse('thing_list')))

        responses.append(c.get(reverse('event', args=['war-1812'])))
        responses.append(c.get(reverse('keyword', args=['wars'])))
        responses.append(c.get(reverse('person', args=['napoleon'])))
        responses.append(c.get(reverse('picture', args=['demoiselles'])))
        responses.append(c.get(reverse('place', args=['north-pole'])))
        responses.append(c.get(reverse('plan', args=['elevation'])))
        responses.append(c.get(reverse('property', args=['brown-hair'])))
        responses.append(c.get(reverse('thing', args=['curling-iron'])))

        self.c = c
        self.responses = responses

    def test_home(self):
        '''
        Home page should load.
        '''

        # test view
        home = HomeView()
        self.assertEqual(home.window_title(), 'Home')
        self.assertEqual(home.page_title(), 'Welcome to Arcfire.')

        # test client results
        response_1 = self.c.get('/')
        response_2 = self.c.get(reverse('home'))
        response_1 == response_2
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_1.content, response_2.content)

        self.assert_in_html(
            response_1, '#page_title', ['Welcome to Arcfire.'], ['Flurble.'])



    def test_urls(self):
        '''
        Primary urls should load.
        '''

        for r in self.responses:
            # check that each url works
            self.assertEqual(r.status_code, 200)

            # decode and make sure each has basic elements
            self.assert_in_html(r, 'nav > div#nav_container > h3',
                ['Navigation'])

    def test_header(self):
        '''Header should exist on every page, and should have all the correct links.'''
        for r in self.responses:
            self.assert_in_html(r, 'header #site_title',
                ['Arcfire'], ['Flurble.'])
            self.assert_in_html(r, 'header #site_search',
                ['Search'])


    def test_footer(self):
        '''Footer should exist, and should have all correct links.'''
        for r in self.responses:
            self.assert_in_html(r, 'footer #user',
                ['User'])

    # results in templates
    def test_nav_relative_model(self):
        '''Model pages should each have relative navigation.'''
        responses = []
        responses.append(self.c.get(reverse('event', args=['war-1812'])))
        responses.append(self.c.get(reverse('keyword', args=['wars'])))
        responses.append(self.c.get(reverse('person', args=['napoleon'])))
        responses.append(self.c.get(reverse('picture', args=['demoiselles'])))
        responses.append(self.c.get(reverse('place', args=['north-pole'])))
        responses.append(self.c.get(reverse('plan', args=['elevation'])))
        responses.append(self.c.get(reverse('property', args=['brown-hair'])))
        responses.append(self.c.get(reverse('thing', args=['curling-iron'])))

        for r in responses:
            self.assert_in_html(r, 'nav > #nav_relative > ul',
                ['Home', 'Up', 'First', 'Last'])

    def test_nav_relative_model_list(self):
        pass

    def test_nav_absolute(self):
        pass

    # views working correctly
    def test_get_nav_relative(self):
        pass

    def test_get_model_template(self):
        pass

    def test_get_template_names(self):
        pass

# test messages

# test templates extend



class AuthCase(TestUtils):
    '''
    Tests covering auth, and other account-type stuff.
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
        self.assert_in_html(login_page, '#page_title', ['Login to Arcfire.'])
        self.assert_in_html(login_page, 'footer #user',
                ['Login'], ['Logout'])

        # Login
        response = self.c.post(reverse('login'),
            {'username': 'wellington', 'password': 'waterloo'}, follow=True,)
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(
            int(self.c.session.get('_auth_user_id')),self.duke.pk)

        # Make sure resulting page is right: correct message, nav changes
        
        self.assert_in_html(response, '#messages', ['Login successful.'])
        self.assert_in_html(response, 'footer #user', ['Logout'], ['Login'])

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