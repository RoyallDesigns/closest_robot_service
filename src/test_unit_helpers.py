import unittest

# Internal Libraries
from helpers import ResponseJSONFormatter, ClosestRobotRequestDispatcher

# Internal Test Libraries
from test_utilities import JSONRequestTestFixtureUtilities


class ResponseJSONFormatterUnitTest(unittest.TestCase):

    def test_get_formatted_response_json(self):
        json_data = ResponseJSONFormatter.get_formatted_response_json(robot_id=1,
                                                                      distance_to_goal=2,
                                                                      battery_level=3)
        expected_json_data = {'robotId': 1,
                              'distanceToGoal': 2,
                              'batteryLevel': 3}

        self.assertEqual(first=json_data, second=expected_json_data)

    def test_get_formatted_error_response_json(self):
        json_data = ResponseJSONFormatter.get_formatted_error_response_json()

        expected_json_data = {'robotId': -9999,
                              'distanceToGoal': -9999,
                              'batteryLevel': -9999}

        self.assertEqual(first=json_data, second=expected_json_data)


class ClosestRobotRequestDispatcherUnitTest(unittest.TestCase):

    def test_is_request_json_valid_returns_false_when_json_is_empty(self):
        self.assertFalse(ClosestRobotRequestDispatcher.is_request_json_valid({}))

    def test_is_request_json_valid_returns_false_when_json_has_wrong_types(self):
        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id='bad_data')
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x='bad_data')
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(y='bad_data')
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

    def test_is_request_json_valid_returns_false_when_json_has_wrong_field_names(self):
        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(load_id_name='wrong_name')
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(x_coordinate_name='wrong_name')
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(y_coordinate_name='wrong_name')
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

    def test_is_request_json_valid_returns_true_when_json_is_correctly_formatted(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                        x=0,
                                                                        y=0)

        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)

        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_is_correctly_formatted_with_extra_data(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                        x=0,
                                                                        y=0)
        valid_json_data['extraField'] = 'extraData'

        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)

        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_contains_load_id_greater_than_equal_to_0(self):
        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=-1)
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=0)
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1)
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_contains_x_y_coordinates_of_any_value(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=-1,
                                                                        y=-1)
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=0,
                                                                        y=0)
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=1,
                                                                        y=1)
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_contains_float_x_y_coordinates(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=-0.5,
                                                                        y=-0.5)
        is_valid = ClosestRobotRequestDispatcher.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()
