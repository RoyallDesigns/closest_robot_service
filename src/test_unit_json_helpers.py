import unittest

# Internal Libraries
from json_helpers import ResponseJSONFormatter, RequestJSONTransformer, RobotDatabaseJSONTransformer

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

        expected_json_data = {'robotId': None,
                              'distanceToGoal': None,
                              'batteryLevel': None}

        self.assertEqual(first=json_data, second=expected_json_data)


class RequestJSONTransformerUnitTest(unittest.TestCase):

    def test_is_request_json_valid_returns_false_when_json_is_empty(self):
        self.assertFalse(RequestJSONTransformer.is_request_json_valid({}))

    def test_is_request_json_valid_returns_false_when_json_has_wrong_types(self):
        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id='bad_data')
        is_valid = RequestJSONTransformer.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x='bad_data')
        is_valid = RequestJSONTransformer.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(y='bad_data')
        is_valid = RequestJSONTransformer.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

    def test_is_request_json_valid_returns_false_when_json_has_wrong_field_names(self):
        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(load_id_name='wrong_name')
        is_valid = RequestJSONTransformer.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(x_coordinate_name='wrong_name')
        is_valid = RequestJSONTransformer.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data_override_names(y_coordinate_name='wrong_name')
        is_valid = RequestJSONTransformer.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

    def test_is_request_json_valid_returns_true_when_json_is_correctly_formatted(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                        x=0,
                                                                        y=0)

        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)

        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_is_correctly_formatted_with_extra_data(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                        x=0,
                                                                        y=0)
        valid_json_data['extraField'] = 'extraData'

        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)

        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_contains_load_id_greater_than_equal_to_0(self):
        invalid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=-1)
        is_valid = RequestJSONTransformer.is_request_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=0)
        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=1)
        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_contains_x_y_coordinates_of_any_value(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=-1,
                                                                        y=-1)
        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=0,
                                                                        y=0)
        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=1,
                                                                        y=1)
        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_request_json_valid_returns_true_when_json_contains_float_x_y_coordinates(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(x=-0.5,
                                                                        y=-0.5)
        is_valid = RequestJSONTransformer.is_request_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_creates_load_with_data_from_request_json(self):
        valid_json_data = JSONRequestTestFixtureUtilities.get_post_data(load_id=200,
                                                                        x=-5.0,
                                                                        y=10.0)
        if RequestJSONTransformer.is_request_json_valid(valid_json_data):
            load = RequestJSONTransformer.create_load_from_request_json(valid_json_data)
            self.assertEqual(first=load.get_id(), second=200)
            self.assertEqual(first=load.get_x_coordinate(), second=-5.0)
            self.assertEqual(first=load.get_y_coordinate(), second=10.0)
        else:
            self.fail('Request JSON Used for Testing is Not Valid.')


class RobotDatabaseJSONTransformerUnitTest(unittest.TestCase):

    @staticmethod
    def get_robot_database_data(robot_id=0, battery_level=100, x=0, y=0):
        return {'robotId': robot_id,
                'batteryLevel': battery_level,
                'x': x,
                'y': y}

    @staticmethod
    def get_robot_database_data_override_names(robot_id_name='robotId',
                                               battery_level_name='batteryLevel',
                                               x_name='x',
                                               y_name='y'):
        return {robot_id_name: 0,
                battery_level_name: 100,
                x_name: 0,
                y_name: 0}

    def test_is_robot_database_json_valid_returns_false_when_json_is_empty(self):
        self.assertFalse(RobotDatabaseJSONTransformer.is_robot_database_json_valid({}))

    def test_is_robot_database_json_valid_returns_false_when_json_has_wrong_types(self):
        invalid_json_data = self.get_robot_database_data(robot_id='bad_data')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = self.get_robot_database_data(battery_level='bad_data')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = self.get_robot_database_data(x='bad_data')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = self.get_robot_database_data(y='bad_data')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

    def test_is_robot_database_json_valid_returns_false_when_json_has_wrong_field_names(self):
        invalid_json_data = self.get_robot_database_data_override_names(robot_id_name='wrong_name')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = self.get_robot_database_data_override_names(battery_level_name='wrong_name')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = self.get_robot_database_data_override_names(x_name='wrong_name')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = self.get_robot_database_data_override_names(y_name='wrong_name')
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

    def test_is_robot_database_json_valid_returns_true_when_json_is_correctly_formatted(self):
        valid_json_data = self.get_robot_database_data(robot_id=1,
                                                       battery_level=98,
                                                       x=2,
                                                       y=5)

        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)

        self.assertTrue(is_valid)

    def test_is_robot_database_json_valid_returns_true_when_json_is_correctly_formatted_with_extra_data(self):
        valid_json_data = self.get_robot_database_data(robot_id=1,
                                                       battery_level=98,
                                                       x=2,
                                                       y=5)
        valid_json_data['extraField'] = 'extraData'

        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)

        self.assertTrue(is_valid)

    def test_is_robot_database_json_valid_returns_true_when_json_contains_robot_id_greater_than_equal_to_0(self):
        invalid_json_data = self.get_robot_database_data(robot_id=-1)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        valid_json_data = self.get_robot_database_data(robot_id=0)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = self.get_robot_database_data(robot_id=1)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_robot_database_json_valid_returns_true_when_json_contains_battery_level_from_0_and_100(self):
        invalid_json_data = self.get_robot_database_data(battery_level=-1)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        invalid_json_data = self.get_robot_database_data(battery_level=101)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(invalid_json_data)
        self.assertFalse(is_valid)

        valid_json_data = self.get_robot_database_data(battery_level=0)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = self.get_robot_database_data(battery_level=50)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = self.get_robot_database_data(battery_level=100)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_robot_database_json_valid_returns_true_when_json_contains_float_battery_level(self):
        valid_json_data = self.get_robot_database_data(battery_level=50.5)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_robot_database_json_valid_returns_true_when_json_contains_x_y_coordinates_of_any_value(self):
        valid_json_data = self.get_robot_database_data(x=-1,
                                                       y=-1)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = self.get_robot_database_data(x=0,
                                                       y=0)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

        valid_json_data = self.get_robot_database_data(x=1,
                                                       y=1)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_is_robot_database_json_valid_returns_true_when_json_contains_float_x_y_coordinates(self):
        valid_json_data = self.get_robot_database_data(x=0.9,
                                                       y=0.9)
        is_valid = RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data)
        self.assertTrue(is_valid)

    def test_creates_robot_with_data_from_robot_database_json(self):
        valid_json_data = self.get_robot_database_data(robot_id=100,
                                                       battery_level=28,
                                                       x=200,
                                                       y=-5)
        if RobotDatabaseJSONTransformer.is_robot_database_json_valid(valid_json_data):
            robot = RobotDatabaseJSONTransformer.create_robot_from_robot_database_json(valid_json_data)
            self.assertEqual(first=robot.get_id(), second=100)
            self.assertEqual(first=robot.get_battery_level(), second=28)
            self.assertEqual(first=robot.get_x_coordinate(), second=200)
            self.assertEqual(first=robot.get_y_coordinate(), second=-5)
        else:
            self.fail('Robot Database JSON Used for Testing is Not Valid.')


if __name__ == '__main__':
    unittest.main()
