import unittest

# Internal Libraries
from calculators import ClosestRobotCalculator
from models import Robot, Load


class ClosestRobotCalculatorTest(unittest.TestCase):

    @staticmethod
    def create_load_with(load_id=0, x_coordinate=0, y_coordinate=0):
        return Load(id=load_id, x_coordinate=x_coordinate, y_coordinate=y_coordinate)

    @staticmethod
    def create_robot_with(robot_id=0, battery_level=100, x_coordinate=0, y_coordinate=0):
        return Robot(id=robot_id,
                     battery_level=battery_level,
                     x_coordinate=x_coordinate,
                     y_coordinate=y_coordinate)

    def test_calculate_closest_robot_for_load_returns_none_for_empty_robot_list(self):
        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=[],
                                                                                load=self.create_load_with())

        self.assertIsNone(closest_robot)

    def test_calculate_closest_robot_for_load_returns_only_robot_for_single_robot_list(self):
        robot = self.create_robot_with(robot_id=22)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=[robot],
                                                                                load=self.create_load_with())

        self.assertEqual(first=closest_robot.get_id(), second=robot.get_id())

    def test_calculate_closest_robot_for_load_returns_closest_robot_for_two_equally_charged_robots(self):
        robot_one = self.create_robot_with(robot_id=20, battery_level=100, x_coordinate=0, y_coordinate=1)
        robot_two = self.create_robot_with(robot_id=40, battery_level=100, x_coordinate=5, y_coordinate=5)
        robots = [robot_one, robot_two]
        load = self.create_load_with(x_coordinate=0, y_coordinate=0)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertEqual(first=closest_robot.get_id(), second=robot_one.get_id())

    def test_calculate_closest_robot_for_load_returns_robot_with_most_charge_for_two_equally_distanced_robots(self):
        robot_one = self.create_robot_with(robot_id=100, battery_level=50, x_coordinate=5, y_coordinate=5)
        robot_two = self.create_robot_with(robot_id=40, battery_level=100, x_coordinate=-5, y_coordinate=-5)
        robots = [robot_one, robot_two]
        load = self.create_load_with(x_coordinate=0, y_coordinate=0)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertEqual(first=closest_robot.get_id(), second=robot_two.get_id())

    def test_calculate_closest_robot_for_load_returns_first_robot_for_two_equally_distanced_equally_charged_robots(self):
        robot_one = self.create_robot_with(robot_id=100, battery_level=100, x_coordinate=3, y_coordinate=3)
        robot_two = self.create_robot_with(robot_id=40, battery_level=100, x_coordinate=-3, y_coordinate=-3)

        robots = [robot_one, robot_two]
        load = self.create_load_with(x_coordinate=0, y_coordinate=0)
        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)
        self.assertEqual(first=closest_robot.get_id(), second=robot_one.get_id())

        robots = [robot_two, robot_one]
        load = self.create_load_with(x_coordinate=0, y_coordinate=0)
        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)
        self.assertEqual(first=closest_robot.get_id(), second=robot_two.get_id())

    def test_calculate_closest_robot_for_load_returns_robot_with_most_charge_within_10_distance_units(self):
        robot_one = self.create_robot_with(robot_id=1, battery_level=50, x_coordinate=0, y_coordinate=1)
        robot_two = self.create_robot_with(robot_id=2, battery_level=60, x_coordinate=0, y_coordinate=3)
        robot_three = self.create_robot_with(robot_id=3, battery_level=70, x_coordinate=0, y_coordinate=5)
        robot_four = self.create_robot_with(robot_id=4, battery_level=80, x_coordinate=0, y_coordinate=7)
        robot_five = self.create_robot_with(robot_id=5, battery_level=90, x_coordinate=0, y_coordinate=9)
        robot_six = self.create_robot_with(robot_id=6, battery_level=95, x_coordinate=0, y_coordinate=10)
        robot_seven = self.create_robot_with(robot_id=7, battery_level=100, x_coordinate=0, y_coordinate=11)
        robots = [robot_one, robot_two, robot_three, robot_four, robot_five, robot_six, robot_seven]
        load = self.create_load_with(x_coordinate=0, y_coordinate=0)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertEqual(first=closest_robot.get_id(), second=robot_six.get_id())

    def test_calculate_closest_robot_for_load_returns_just_closest_robot_if_none_within_10_distance_units(self):
        robot_one = self.create_robot_with(robot_id=1, battery_level=100, x_coordinate=0, y_coordinate=-30)
        robot_two = self.create_robot_with(robot_id=2, battery_level=20, x_coordinate=0, y_coordinate=-20)
        robot_three = self.create_robot_with(robot_id=3, battery_level=100, x_coordinate=0, y_coordinate=-40)
        robots = [robot_one, robot_two, robot_three]
        load = self.create_load_with(x_coordinate=0, y_coordinate=0)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertEqual(first=closest_robot.get_id(), second=robot_two.get_id())

    def test_calculate_closest_robot_for_load_returns_robot_right_at_location_if_only_within_10_distance_units(self):
        robot_one = self.create_robot_with(robot_id=1, x_coordinate=0, y_coordinate=100)
        robot_two = self.create_robot_with(robot_id=2, x_coordinate=0, y_coordinate=200)
        robot_three = self.create_robot_with(robot_id=3, x_coordinate=0, y_coordinate=10)
        robots = [robot_one, robot_two, robot_three]
        load = self.create_load_with(x_coordinate=0, y_coordinate=10)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertEqual(first=closest_robot.get_id(), second=robot_three.get_id())

    def test_calculate_closest_robot_for_load_returns_robot_right_at_location_if_only_within_10_distance_units(self):
        robot_one = self.create_robot_with(robot_id=1, x_coordinate=0, y_coordinate=100)
        robot_two = self.create_robot_with(robot_id=2, x_coordinate=0, y_coordinate=200)
        robot_three = self.create_robot_with(robot_id=3, x_coordinate=0, y_coordinate=10)
        robots = [robot_one, robot_two, robot_three]
        load = self.create_load_with(x_coordinate=0, y_coordinate=10)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertEqual(first=closest_robot.get_id(), second=robot_three.get_id())

    def test_calculate_closest_robot_for_load_ignores_robot_at_location_if_others_within_10_distance_units_have_more_charge(self):
        robot_one = self.create_robot_with(robot_id=1, battery_level=50, x_coordinate=0, y_coordinate=12)
        robot_two = self.create_robot_with(robot_id=2, battery_level=5, x_coordinate=0, y_coordinate=11)
        robot_three = self.create_robot_with(robot_id=3, battery_level=1, x_coordinate=0, y_coordinate=10)
        robots = [robot_one, robot_two, robot_three]
        load = self.create_load_with(x_coordinate=0, y_coordinate=10)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertEqual(first=closest_robot.get_id(), second=robot_one.get_id())

    def test_calculate_closest_robot_for_load_ignores_robots_with_0_battery(self):
        robot_one = self.create_robot_with(robot_id=1, battery_level=0, x_coordinate=10, y_coordinate=0)
        robot_two = self.create_robot_with(robot_id=2, battery_level=0, x_coordinate=20, y_coordinate=0)
        robot_three = self.create_robot_with(robot_id=3, battery_level=0, x_coordinate=30, y_coordinate=0)
        robots = [robot_one, robot_two, robot_three]
        load = self.create_load_with(x_coordinate=10, y_coordinate=0)

        closest_robot = ClosestRobotCalculator.calculate_closest_robot_for_load(robots=robots,
                                                                                load=load)

        self.assertIsNone(closest_robot)


if __name__ == '__main__':
    unittest.main()
