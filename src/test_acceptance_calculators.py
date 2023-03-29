import unittest

# Internal Libraries
from calculators import ClosestRobotCalculator

# Internal Test Libraries
from test_utilities import JSONRobotDatabaseDataTextFixtureUtilities, JSONRequestTestFixtureUtilities


class ClosestRobotCalculatorAcceptanceTest(unittest.TestCase):

    def test_calculate_closest_robot_for_load_from_json_format_returns_none_if_nothing_is_available(self):
        load_json = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                  x=0,
                                                                  y=10)
        robots_json = []

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                                 load_json=load_json)

        self.assertIsNone(closest_robot)

    def test_calculate_closest_robot_for_load_from_json_format_returns_what_is_available_if_only_one_robot_is_available(self):
        load_json = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                  x=0,
                                                                  y=10)
        robot_1_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=20,
                                                                                         battery_level=100,
                                                                                         x=200,
                                                                                         y=200)
        robots_json = [robot_1_json]

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                                 load_json=load_json)

        self.assertEqual(first=closest_robot.get_id(), second=20)

    def test_calculate_closest_robot_for_load_from_json_format_returns_closest_robot(self):
        load_json = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                  x=0,
                                                                  y=10)
        robot_1_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=1,
                                                                                         battery_level=100,
                                                                                         x=0,
                                                                                         y=11)
        robot_2_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=2,
                                                                                         battery_level=100,
                                                                                         x=0,
                                                                                         y=12)
        robot_3_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=3,
                                                                                         battery_level=100,
                                                                                         x=0,
                                                                                         y=13)
        robots_json = [robot_1_json, robot_2_json, robot_3_json]

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                                 load_json=load_json)

        self.assertEqual(first=closest_robot.get_id(), second=1)

    def test_calculate_closest_robot_for_load_from_json_format_returns_closest_robot_within_10_unit_distance_with_greatest_charge(self):
        load_json = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                  x=0,
                                                                  y=10)
        robot_1_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=1,
                                                                                         battery_level=20,
                                                                                         x=0,
                                                                                         y=10)
        robot_2_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=2,
                                                                                         battery_level=50,
                                                                                         x=0,
                                                                                         y=15)
        robot_3_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=3,
                                                                                         battery_level=100,
                                                                                         x=0,
                                                                                         y=22)
        robots_json = [robot_1_json, robot_2_json, robot_3_json]

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                                 load_json=load_json)

        self.assertEqual(first=closest_robot.get_id(), second=2)

    def test_calculate_closest_robot_for_load_from_json_format_ignores_robots_with_no_charge(self):
        load_json = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                  x=0,
                                                                  y=10)
        robot_1_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=1,
                                                                                         battery_level=0,
                                                                                         x=0,
                                                                                         y=10)
        robot_2_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=2,
                                                                                         battery_level=0,
                                                                                         x=0,
                                                                                         y=15)
        robot_3_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=3,
                                                                                         battery_level=20,
                                                                                         x=0,
                                                                                         y=100)
        robots_json = [robot_1_json, robot_2_json, robot_3_json]

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                                 load_json=load_json)

        self.assertEqual(first=closest_robot.get_id(), second=3)

    def test_calculate_closest_robot_for_load_from_json_format_ignores_invalid_robots(self):
        load_json = JSONRequestTestFixtureUtilities.get_post_data(load_id=1,
                                                                  x=0,
                                                                  y=10)
        robot_1_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=1,
                                                                                         battery_level=100,
                                                                                         x=0,
                                                                                         y=200)
        robot_2_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=-999,
                                                                                         battery_level=-999,
                                                                                         x=0,
                                                                                         y=5)
        robots_json = [robot_1_json, robot_2_json]

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                                 load_json=load_json)

        self.assertEqual(first=closest_robot.get_id(), second=1)

    def test_calculate_closest_robot_for_load_from_json_format_throws_error_on_invalid_load(self):
        load_json = JSONRequestTestFixtureUtilities.get_post_data(load_id=-999,
                                                                  x=0,
                                                                  y=10)
        robot_1_json = JSONRobotDatabaseDataTextFixtureUtilities.get_robot_database_data(robot_id=1,
                                                                                         battery_level=100,
                                                                                         x=0,
                                                                                         y=200)
        robots_json = [robot_1_json]

        with self.assertRaises(ValueError):
            ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                     load_json=load_json)


if __name__ == '__main__':
    unittest.main()
