from django.test import TestCase, RequestFactory
from arcfire.views.core import *


class GlobalViewTestCase(TestCase):
    '''
    Unit tests for shared functionality.
    '''

    def setUp(self):
        self.views = [
            {'view': ViewMixin,
             'page_title': 'Arcfire',
             'window_title': 'Arcfire'},
            {'view': HomeView,
             'page_title': 'Welcome to Arcfire',
             'window_title': 'Home'},
            {'view': LoginView,
             'page_title': 'Login to Arcfire',
             'window_title': 'Login'},
            {'view': SearchView,
             'page_title': 'Search Results',
             'window_title': 'Search Results'},
        ]

    def test_page_titles(self):
        '''
        Should each provide a default page title.
        '''
        for v in self.views:
            instance = v['view']()
            self.assertEqual(instance.page_title(), v['page_title'])


    def test_window_titles(self):
        '''
        Should each provide a default window title.
        '''
        for v in self.views:
            instance = v['view']()
            self.assertEqual(instance.window_title(), v['window_title'])


class ViewMixinTestCase(TestCase):
    '''
    Unit tests covering ViewMixin. 
    '''

    def setUp(self):
        self.obj = ViewMixin()

    def test_model_list(self):
        '''
        Should support all major models and other view methods. 
        '''
        model_list = self.obj.model_list()
        self.assertEqual(len(model_list), 8)
        for d in model_list:
            self.assertTrue('model' in d.keys())
            self.assertTrue('search_fields' in d.keys())
            self.assertTrue('template' in d.keys())

    def test_nav_relative(self):
        '''
        Should provide basic relative navigation links.
        '''
        nav = self.obj.nav_relative()
        for d in nav:
            self.assertIn('name', d.keys())
            self.assertIn('url', d.keys())


class HomeTestCase(TestCase):
    '''
    Unit tests for HomeView covered in other unit tests.
    '''


class LoginTestCase(TestCase):
    '''
    Unit tests for Login not separable from functional tests.
    '''
    

class LogoutTestCase(TestCase):
    '''
    Unit tests for Logout not separable from functional tests.
    '''


class SearchTestCase(TestCase):
    '''
    Unit tests covering search.
    '''
    # haven't figured how to do this yet!

    def setUp(self):
        factory = RequestFactory()
        self.request = factory.post('/search', {'q': 'war'})
        # self.response = SearchView.as_view().search_results()(self.request)

    def test_search_results(self):
        '''
        Should provide accurate search results.
        '''
        # Haven't figured out how to unit-test yet.
        # self.assertIn('abcd', self.response)


class ModelViewTestCase(TestCase):
    '''
    Tests covering the ModelView.
    '''
    # haven't figured how to do this yet!

    def setUp(self):
        pass


class ModelListViewTestCase(TestCase):
    '''
    Tests covering the ModelView.
    '''
    # haven't figured how to do this yet!

    def setUp(self):
        pass
