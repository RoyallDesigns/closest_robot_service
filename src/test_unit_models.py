import unittest

# Internal Libraries
from models import Robot, Load


class RobotUnitTest(unittest.TestCase):

    @staticmethod
    def create_robot_with(id=0, battery_level=100, x_coordinate=0, y_coordinate=0):
        return Robot(id=id,
                     battery_level=battery_level,
                     x_coordinate=x_coordinate,
                     y_coordinate=y_coordinate)

    def test_robot_has_an_id_to_set_and_get(self):
        robot = self.create_robot_with(id=101)
        self.assertEqual(first=robot.get_id(), second=101)

    def test_robot_has_a_battery_level_to_set_and_get(self):
        robot = self.create_robot_with(battery_level=50)
        self.assertEqual(first=robot.get_battery_level(), second=50)

    def test_robot_has_an_x_and_y_coordinate_to_set_and_get(self):
        robot = self.create_robot_with(x_coordinate=10, y_coordinate=20)
        self.assertEqual(first=robot.get_x_coordinate(), second=10)
        self.assertEqual(first=robot.get_y_coordinate(), second=20)

    def test_robot_has_a_distance_to_load_that_is_none_if_unset(self):
        robot = self.create_robot_with()
        self.assertIsNone(robot.get_distance_to_load())

    def test_robot_has_a_distance_to_load_to_set_and_get(self):
        robot = self.create_robot_with()
        robot.set_distance_to_load(10)
        self.assertEqual(first=robot.get_distance_to_load(), second=10)


class LoadUnitTest(unittest.TestCase):

    @staticmethod
    def create_load_with(id=0, x_coordinate=0, y_coordinate=0):
        return Load(id=id,
                    x_coordinate=x_coordinate,
                    y_coordinate=y_coordinate)

    def test_load_has_an_id_to_set_and_get(self):
        load = self.create_load_with(id=99)
        self.assertEqual(first=load.get_id(), second=99)

    def test_load_has_an_x_and_y_coordinate_to_set_and_get(self):
        load = self.create_load_with(x_coordinate=1, y_coordinate=2)
        self.assertEqual(first=load.get_x_coordinate(), second=1)
        self.assertEqual(first=load.get_y_coordinate(), second=2)


if __name__ == '__main__':
    unittest.main()
