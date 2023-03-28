
import unittest
import requests

# Internal Test Libraries
from test_utilities import JSONRequestTestFixtureUtilities


class ClosestRobotServiceAcceptanceTest(unittest.TestCase):
    _ENDPOINT_URL = 'http://localhost:5000/api/robots/closest'

    def test_entirely_different_post_data_leads_to_error_response(self):
        response = requests.post(url=self._ENDPOINT_URL, data='bad_data')

        self.assertEqual(first=response.status_code, second=415)  # Unsupported Media Type

        expected_response_json = {'robotId': -9999,
                                  'distanceToGoal': -9999,
                                  'batteryLevel': -9999}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_empty_post_leads_to_error_response(self):
        response = requests.post(url=self._ENDPOINT_URL, json={})

        self.assertEqual(first=response.status_code, second=415)  # Unsupported Media Type

        expected_response_json = {'robotId': -9999,
                                  'distanceToGoal': -9999,
                                  'batteryLevel': -9999}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_properly_fielded_post_data_with_bad_data_leads_to_error_response(self):
        improperly_populated_data = JSONRequestTestFixtureUtilities.get_post_data(load_id='bad_data',
                                                                                  x='bad_data',
                                                                                  y='bad_data')

        response = requests.post(url=self._ENDPOINT_URL,
                                 json=improperly_populated_data)

        self.assertEqual(first=response.status_code, second=415)  # Unsupported Media Type

        expected_response_json = {'robotId': -9999,
                                  'distanceToGoal': -9999,
                                  'batteryLevel': -9999}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_properly_fielded_post_data_with_bad_data_names_leads_to_error_response(self):
        improperly_named_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(load_id_name='bad_name',
                                                                                             x_coordinate_name='bad_name',
                                                                                             y_coordinate_name='bad_name')

        response = requests.post(url=self._ENDPOINT_URL,
                                 json=improperly_named_data)

        self.assertEqual(first=response.status_code, second=415)  # Unsupported Media Type

        expected_response_json = {'robotId': -9999,
                                  'distanceToGoal': -9999,
                                  'batteryLevel': -9999}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_get_data_at_endpoint_leads_to_error_response(self):
        response = requests.get(self._ENDPOINT_URL)

        self.assertEqual(first=response.status_code, second=405)  # Method Not Allowed


if __name__ == '__main__':
    unittest.main()
