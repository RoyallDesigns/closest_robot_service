
class Robot(object):

    def __init__(self, id, battery_level, x_coordinate, y_coordinate):
        self._id = id
        self._battery_level = battery_level
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self._distance_to_load = None

    def get_id(self):
        return int(self._id)

    def get_battery_level(self):
        return self._battery_level

    def get_x_coordinate(self):
        return self._x_coordinate

    def get_y_coordinate(self):
        return self._y_coordinate

    def set_distance_to_load(self, distance_to_load):
        self._distance_to_load = distance_to_load

    def get_distance_to_load(self):
        return self._distance_to_load


class Load(object):

    def __init__(self, id, x_coordinate, y_coordinate):
        self._id = id
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate

    def get_id(self):
        return int(self._id)

    def get_x_coordinate(self):
        return self._x_coordinate

    def get_y_coordinate(self):
        return self._y_coordinate
