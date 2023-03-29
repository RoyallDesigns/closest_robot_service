
import unittest
import requests
import threading

# Internal Libraries
import closest_robot_service

# Internal Test Libraries
from test_utilities import JSONRequestTestFixtureUtilities


class ClosestRobotServiceAcceptanceTest(unittest.TestCase):
    _ENDPOINT_URL = 'http://localhost:5000/api/robots/closest'
    _SERVICE_THREAD = threading.Thread(target=closest_robot_service.main, daemon=True)

    @classmethod
    def setUpClass(cls):
        cls._SERVICE_THREAD.start()

    def test_entirely_different_post_data_leads_to_error_response(self):
        response = requests.post(url=self._ENDPOINT_URL, data='bad_data')

        self.assertEqual(first=response.status_code, second=415)  # Unsupported Media Type

        expected_response_json = {'robotId': None,
                                  'distanceToGoal': None,
                                  'batteryLevel': None}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_empty_post_leads_to_error_response(self):
        response = requests.post(url=self._ENDPOINT_URL, json={})

        self.assertEqual(first=response.status_code, second=400)  # Bad Request

        expected_response_json = {'robotId': None,
                                  'distanceToGoal': None,
                                  'batteryLevel': None}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_properly_fielded_post_data_with_bad_data_leads_to_error_response(self):
        improperly_populated_data = JSONRequestTestFixtureUtilities.get_post_data(load_id='bad_data',
                                                                                  x='bad_data',
                                                                                  y='bad_data')

        response = requests.post(url=self._ENDPOINT_URL, json=improperly_populated_data)

        self.assertEqual(first=response.status_code, second=400)  # Bad Request

        expected_response_json = {'robotId': None,
                                  'distanceToGoal': None,
                                  'batteryLevel': None}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_properly_fielded_post_data_with_bad_data_names_leads_to_error_response(self):
        improperly_named_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(load_id_name='bad_name',
                                                                                             x_coordinate_name='bad_name',
                                                                                             y_coordinate_name='bad_name')

        response = requests.post(url=self._ENDPOINT_URL, json=improperly_named_data)

        self.assertEqual(first=response.status_code, second=400)  # Bad Request

        expected_response_json = {'robotId': None,
                                  'distanceToGoal': None,
                                  'batteryLevel': None}
        self.assertEqual(first=response.json(), second=expected_response_json)

    def test_get_data_at_endpoint_leads_to_error_response(self):
        response = requests.get(self._ENDPOINT_URL)

        self.assertEqual(first=response.status_code, second=405)  # Method Not Allowed

    def test_valid_post_data_leads_to_valid_response(self):
        valid_json_input_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                              x=2,
                                                                              y=3)

        response = requests.post(url=self._ENDPOINT_URL, json=valid_json_input_data)

        self.assertEqual(first=response.status_code, second=200)  # OK

        response_json = response.json()
        for response_key in ['robotId', 'distanceToGoal', 'batteryLevel']:
            response_value = response_json[response_key]
            self.assertGreaterEqual(a=response_value, b=0)

    def test_valid_post_data_with_extraneous_fields_still_leads_to_valid_response(self):
        valid_json_input_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                              x=2,
                                                                              y=3)
        valid_json_input_data['extraField'] = 'extraData'

        response = requests.post(url=self._ENDPOINT_URL, json=valid_json_input_data)

        self.assertEqual(first=response.status_code, second=200)  # OK

        response_json = response.json()
        for response_key in ['robotId', 'distanceToGoal', 'batteryLevel']:
            response_value = response_json[response_key]
            self.assertGreaterEqual(a=response_value, b=0)

    def test_post_data_with_negative_load_id_leads_to_error_response(self):
        data_with_improper_load_id = JSONRequestTestFixtureUtilities.get_post_data(load_id=-101)

        response = requests.post(url=self._ENDPOINT_URL, json=data_with_improper_load_id)

        self.assertEqual(first=response.status_code, second=400)  # Bad Request

        expected_response_json = {'robotId': None,
                                  'distanceToGoal': None,
                                  'batteryLevel': None}
        self.assertEqual(first=response.json(), second=expected_response_json)


if __name__ == '__main__':
    unittest.main()
