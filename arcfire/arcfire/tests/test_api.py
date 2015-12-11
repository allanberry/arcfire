from django.test import TestCase, Client
from arcfire.views.api import *
from django.core.urlresolvers import reverse


class GlobalViewTestCase(TestCase):
    '''
    Unit tests for shared functionality.
    '''

    def setUp(self):
        self.c = Client()

        api_names = [
            # 'card_api',
            # 'event_api',
            # 'keyword_api',
            # 'person_api',
            # 'picture_api',
            # 'place_api',
            # 'plan_api',
            # 'property_api',
            # 'thing_api',
            # 'card_list_api',
            # 'event_list_api',
            # 'keyword_list_api',
            # 'person_list_api',
            # 'picture_list_api',
            # 'place_list_api',
            # 'plan_list_api',
            # 'property_list_api',
            # 'thing_list_api',
        ]

        # some canned responses
        responses = []
        for api_name in api_names:
            responses.append(self.c.get(reverse(api_name)))
        self.responses = responses

    def test_api_loads(self):
        '''
        Each API response should load.
        '''
        for r in self.responses:
            self.assertEqual(r.status_code, 200)
