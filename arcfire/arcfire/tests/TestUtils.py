import lxml.html
from lxml.cssselect import CSSSelector
from django.test import TestCase, Client

import json

class TestUtils(TestCase):

    def get_elements(self, html, selector):
        '''
        Parse html for all elements which conform to a selector, and return them as a list of strings.
        '''
        tree = lxml.html.fromstring(html)
        sel = CSSSelector(selector)

        results = sel(tree)

        text_results = []
        for r in results:
            text_results.append(lxml.html.tostring(r))

        return text_results


    def assert_in_html(self, html, selector, yes=[], no=[]):
        '''
        Make sure every 'yes' element exists in html, and every 'no' element does not.  
        Limited by selector, which should indicate singular elements (id rather than class).
        '''
        elements = self.get_elements(html, selector)
        # each yes must be in every element
        # each no must not be in any element
        for element in elements:
            element = element.decode('utf-8')
            for item in yes:
                self.assertIn(item, element)
            for item in no:
                self.assertNotIn(item, element)
