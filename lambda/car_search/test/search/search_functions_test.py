import unittest

from unittest.mock import MagicMock, Mock, patch, ANY

from search.search_functions import search_exact_match, search_similar_match


class SearchExactMatchTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_context = Mock()

    def testSearchExactMatch(self):
        self.mock_event = {"operation": "search_exact_match", 'car_name_query': 'ford torino'}
        self.expected_search_result = [{
           'Name': 'ford torino',
           'Miles_per_Gallon': 17,
           'Cylinders': 8,
           'Displacement': 302,
           'Horsepower': 140,
           'Weight_in_lbs': 3449,
           'Acceleration': 10.5,
           'Year': '1970-01-01',
           'Origin': 'USA'
        }]
        search_result = search_exact_match(self.mock_event)
        assert search_result == self.expected_search_result, 'A ford torino is found and returned'

    def testSearchSimilarMatch(self):
        self.mock_event = {"operation": "search_similar_match", 'car_name_query': 'rx3'}
        self.expected_search_result = [{
           'Name': 'maxda rx3',
           'Miles_per_Gallon': 18,
           'Cylinders': 3,
           'Displacement': 70,
           'Horsepower': 90,
           'Weight_in_lbs': 2124,
           'Acceleration': 13.5,
           'Year': '1973-01-01',
           'Origin': 'Japan'
        }]
        search_result = search_similar_match(self.mock_event)
        assert search_result == self.expected_search_result, 'A a list of valid matches is found and returned'