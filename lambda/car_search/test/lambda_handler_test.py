import unittest

from unittest.mock import MagicMock, Mock, patch, ANY

from lambda_handler import lambda_handler

class LambdaHandlerTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_context = Mock()

    def testSearchExactMatchInvoked(self):
        with patch('search.search_functions.search_exact_match') as search_exact_match_mock:
            self.mock_event = {"operation": "search_exact_match", 'car_name_query': 'ford torino'}
            lambda_handler(self.mock_event, self.mock_context)
            search_exact_match_mock.assert_called_once(), 'The search_exact_match function is invoked'

    def testSearchSimilarMatchInvoked(self):
        with patch('search.search_functions.search_similar_match') as search_similar_match_mock:
            self.mock_event = {"operation": "search_similar_match", "car_name_query": "ford"}
            lambda_handler(self.mock_event, self.mock_context)
            search_similar_match_mock.assert_called_once(), 'The search_similar_match function is invoked'