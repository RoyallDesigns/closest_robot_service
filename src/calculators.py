import math


class ClosestRobotCalculator(object):
    _DISTANCE_WINDOW = 10

    @staticmethod
    def _calculate_distance_between_robot_and_load(robot, load):
        x_1 = robot.get_x_coordinate()
        y_1 = robot.get_y_coordinate()
        x_2 = load.get_x_coordinate()
        y_2 = load.get_y_coordinate()
        return math.sqrt(math.pow((x_2 - x_1), 2) + math.pow((y_2 - y_1), 2))

    @classmethod
    def calculate_closest_robot_for_load(cls, robots, load):
        for robot in robots:
            distance_to_load = cls._calculate_distance_between_robot_and_load(robot=robot, load=load)
            robot.set_distance_to_load(distance_to_load)
        robots_that_have_non_zero_battery = [robot for robot in robots if robot.get_battery_level()]
        sorted_robots_based_on_distances_to_loads = sorted(
            robots_that_have_non_zero_battery, key=lambda robot: robot.get_distance_to_load())
        sorted_robots_within_window = [robot for robot in sorted_robots_based_on_distances_to_loads
                                       if robot.get_distance_to_load() <= cls._DISTANCE_WINDOW]
        closest_robot_with_most_battery = None
        if len(sorted_robots_based_on_distances_to_loads):
            closest_robot_with_most_battery = sorted_robots_based_on_distances_to_loads[0]
        if len(sorted_robots_within_window):
            closest_robot_with_most_battery = sorted_robots_within_window[0]
        for i in range(1, len(sorted_robots_within_window)):
            current_robot = sorted_robots_within_window[i]
            if current_robot.get_battery_level() > closest_robot_with_most_battery.get_battery_level():
                closest_robot_with_most_battery = current_robot
        return closest_robot_with_most_battery
