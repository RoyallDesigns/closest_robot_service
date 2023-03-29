import unittest

# Internal Libraries
from json_retriever import JSONRetriever


class JSONRetrieverIntegrationTest(unittest.TestCase):
    _URL_ENDPOINT = 'https://60c8ed887dafc90017ffbd56.mockapi.io/robots'
    _UNCONFIGURED_ENDPOINT = 'https://svtrobotics.free.beeceptor.com/robots'

    def test_can_retrieve_json_from_url_with_success(self):
        json_retriever = JSONRetriever(self._URL_ENDPOINT)

        is_successful, json_data = json_retriever.get_json_data()

        self.assertTrue(is_successful)
        self.assertIsNotNone(json_data)

    def test_handles_improper_url_by_returning_error(self):
        json_retriever = JSONRetriever('some_garabge_url')

        is_successful, json_data = json_retriever.get_json_data()

        self.assertFalse(is_successful)
        self.assertIsNone(json_data)

    def test_handles_unconfigured_url_endpoint_by_returning_error(self):
        json_retriever = JSONRetriever(self._UNCONFIGURED_ENDPOINT)

        is_successful, json_data = json_retriever.get_json_data()

        self.assertFalse(is_successful)
        self.assertIsNone(json_data)

    # These Tests Could Be Expanded Based on Additional Cases of Network / Endpoint Failure


if __name__ == '__main__':
    unittest.main()
