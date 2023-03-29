
# Internal Libraries
from models import Load, Robot


class ResponseJSONFormatter(object):
    _ROBOT_ID_KEY = 'robotId'
    _DISTANCE_TO_GOAL_KEY = 'distanceToGoal'
    _BATTERY_LEVEL_KEY = 'batteryLevel'
    _RESPONSE_JSON_ERROR_VALUE = None

    @classmethod
    def get_formatted_response_json(cls, robot_id, distance_to_goal, battery_level):
        return {cls._ROBOT_ID_KEY: robot_id,
                cls._DISTANCE_TO_GOAL_KEY: distance_to_goal,
                cls._BATTERY_LEVEL_KEY: battery_level}

    @classmethod
    def get_formatted_error_response_json(cls):
        return cls.get_formatted_response_json(robot_id=cls._RESPONSE_JSON_ERROR_VALUE,
                                               distance_to_goal=cls._RESPONSE_JSON_ERROR_VALUE,
                                               battery_level=cls._RESPONSE_JSON_ERROR_VALUE)


class RequestJSONTransformer(object):
    _LOAD_ID_KEY = 'loadId'
    _X_COORDINATE_KEY = 'x'
    _Y_COORDINATE_KEY = 'y'

    @classmethod
    def _desired_keys_exist_in_json(cls, request_json):
        request_json_keys = request_json.keys()
        keys_exist = cls._LOAD_ID_KEY in request_json_keys and \
            cls._X_COORDINATE_KEY in request_json_keys and \
            cls._Y_COORDINATE_KEY in request_json_keys
        return keys_exist

    @classmethod
    def _desired_value_ranges_exist_in_json(cls, request_json):
        load_id = request_json[cls._LOAD_ID_KEY]
        x_coordinate = request_json[cls._X_COORDINATE_KEY]
        y_coordinate = request_json[cls._Y_COORDINATE_KEY]
        load_id_is_int = (type(load_id) == int)
        coordinates_are_numbers = ((type(x_coordinate) == int) or (type(x_coordinate) == float)) and \
                                  ((type(y_coordinate) == int) or (type(y_coordinate) == float))
        return load_id_is_int and (load_id >= 0) and coordinates_are_numbers

    @classmethod
    def is_request_json_valid(cls, request_json):
        return cls._desired_keys_exist_in_json(request_json) and cls._desired_value_ranges_exist_in_json(request_json)

    @classmethod
    def create_load_from_request_json(cls, request_json):
        load_id = request_json[cls._LOAD_ID_KEY]
        x_coordinate = request_json[cls._X_COORDINATE_KEY]
        y_coordinate = request_json[cls._Y_COORDINATE_KEY]
        return Load(id=load_id,
                    x_coordinate=x_coordinate,
                    y_coordinate=y_coordinate)


class RobotDatabaseJSONTransformer(object):
    _ROBOT_ID_KEY = 'robotId'
    _BATTERY_LEVEL_KEY = 'batteryLevel'
    _X_COORDINATE_KEY = 'x'
    _Y_COORDINATE_KEY = 'y'

    @classmethod
    def _desired_keys_exist_in_json(cls, robot_database_json):
        robot_database_json_keys = robot_database_json.keys()
        keys_exist = cls._ROBOT_ID_KEY in robot_database_json_keys and \
            cls._BATTERY_LEVEL_KEY in robot_database_json_keys and \
            cls._X_COORDINATE_KEY in robot_database_json_keys and \
            cls._Y_COORDINATE_KEY in robot_database_json_keys
        return keys_exist

    @classmethod
    def _desired_value_ranges_exist_in_json(cls, robot_database_json):
        robot_id = robot_database_json[cls._ROBOT_ID_KEY]
        battery_level = robot_database_json[cls._BATTERY_LEVEL_KEY]
        x_coordinate = robot_database_json[cls._X_COORDINATE_KEY]
        y_coordinate = robot_database_json[cls._Y_COORDINATE_KEY]
        robot_id_is_int = (type(robot_id) == int)
        battery_level_is_number = ((type(battery_level) == int) or (type(battery_level) == float))
        coordinates_are_numbers = ((type(x_coordinate) == int) or (type(x_coordinate) == float)) and \
                                  ((type(y_coordinate) == int) or (type(y_coordinate) == float))
        return robot_id_is_int and (robot_id >= 0) and \
            battery_level_is_number and (battery_level >= 0) and (battery_level <= 100) and\
            coordinates_are_numbers

    @classmethod
    def is_robot_database_json_valid(cls, robot_database_json):
        return cls._desired_keys_exist_in_json(robot_database_json) and \
            cls._desired_value_ranges_exist_in_json(robot_database_json)

    @classmethod
    def create_robot_from_robot_database_json(cls, robot_database_json):
        robot_id = robot_database_json[cls._ROBOT_ID_KEY]
        battery_level = robot_database_json[cls._BATTERY_LEVEL_KEY]
        x_coordinate = robot_database_json[cls._X_COORDINATE_KEY]
        y_coordinate = robot_database_json[cls._Y_COORDINATE_KEY]
        return Robot(id=robot_id,
                     battery_level=battery_level,
                     x_coordinate=x_coordinate,
                     y_coordinate=y_coordinate)
