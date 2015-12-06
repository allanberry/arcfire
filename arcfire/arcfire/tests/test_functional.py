import json
import lxml.html
from arcfire.models import *
from arcfire.views import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from lxml.cssselect import CSSSelector


class HTMLResultMixin(object):
    '''
    Collection of a few tests to test HTML result.
    '''

    def get_elements(self, html, selector):
        '''
        Parse html for all elements which conform to a selector,
        and return them as a list of strings.
        '''
        tree = lxml.html.fromstring(html)
        sel = CSSSelector(selector)

        results = sel(tree)

        text_results = []
        for r in results:
            text_results.append(lxml.html.tostring(r))

        return text_results


    def assert_in_html(self, response, selector, yes=[], no=[],
        encoding='utf-8'):
        '''
        Make sure every 'yes' element exists in html, and every 'no' element
        does not, limited by selector.  Intended for singular elements.
        '''
        content = response.content.decode(encoding)
        elements = self.get_elements(content, selector)
        # each yes must be in every element
        # each no must not be in any element
        for element in elements:
            element = element.decode(encoding)
            for item in yes:
                self.assertIn(item, element)
            for item in no:
                self.assertNotIn(item, element)


class GlobalTestCase(HTMLResultMixin, TestCase):
    '''
    Horizontal, Sitewide tests for common elements across the site.
    '''
    def setUp(self):
        self.c = Client()

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
        responses.append(self.c.get(reverse('home')))
        responses.append(self.c.get(reverse('login')))

        responses.append(self.c.get(reverse('event_list')))
        responses.append(self.c.get(reverse('keyword_list')))
        responses.append(self.c.get(reverse('person_list')))
        responses.append(self.c.get(reverse('picture_list')))
        responses.append(self.c.get(reverse('place_list')))
        responses.append(self.c.get(reverse('plan_list')))
        responses.append(self.c.get(reverse('property_list')))
        responses.append(self.c.get(reverse('thing_list')))
        responses.append(self.c.get(reverse('search')))
        self.responses = responses

        # the following response subset separated out,
        # because has more specific functionality
        model_responses = [] 
        model_responses.append(self.c.get(reverse('event', args=['war-1812'])))
        model_responses.append(self.c.get(reverse('keyword', args=['wars'])))
        model_responses.append(self.c.get(reverse('person', args=['napoleon'])))
        model_responses.append(self.c.get(reverse('picture', args=['demoiselles'])))
        model_responses.append(self.c.get(reverse('place', args=['north-pole'])))
        model_responses.append(self.c.get(reverse('plan', args=['elevation'])))
        model_responses.append(self.c.get(reverse('property', args=['brown-hair'])))
        model_responses.append(self.c.get(reverse('thing', args=['curling-iron'])))
        self.model_responses = model_responses

        # all should be available in self.responses, however
        self.responses.extend(model_responses)

    def test_home(self):
        '''
        Home page should load.
        '''

        # test client results
        response_1 = self.c.get('/')
        response_2 = self.c.get(reverse('home'))
        response_1 == response_2
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_1.content, response_2.content)


    def test_urls(self):
        '''
        Urls should load.
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
    def test_nav_relative(self):
        '''
        All pages should have relative navigation.
        Model pages should have more thorough relative navigation.
        '''
        for r in self.responses:
            self.assert_in_html(r, 'nav > #nav_relative > ul',
                ['Home'], ['Flurm'])

        # this should only work for Model pages
        for r in self.model_responses:
            self.assert_in_html(r, 'nav > #nav_relative > ul',
                ['Home', 'Up', 'First', 'Last'])


    def test_nav_absolute(self):
        '''
        All pages should have absolute navigation.
        '''
        for r in self.responses:
            self.assert_in_html(r, 'nav > #nav_absolute > ul',
                ['Home', 'Search', 'Keywords', 'People', 'Pictures',
                 'Places', 'Plans', 'Properties', 'Things'],
                ['First', 'Next', 'Prev', 'Up', 'Last', 'Down'])

    def test_window_titles(self):
        '''
        All pages should have accurate window titles.
        '''
        for r in self.responses:
            self.assert_in_html(r, 'nav > #nav_absolute > ul',
                ['Home', 'Search', 'Keywords', 'People', 'Pictures',
                 'Places', 'Plans', 'Properties', 'Things'],
                ['First', 'Next', 'Prev', 'Up', 'Last', 'Down'])


class AuthTestCase(HTMLResultMixin, TestCase):
    '''
    Tests covering auth: login/logout.
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
        self.assert_in_html(login_page, '#page_title', ['Login'])
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
