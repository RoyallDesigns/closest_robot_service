

class ResponseJSONFormatter(object):
    _RESPONSE_JSON_ERROR_VALUE = -9999

    @classmethod
    def get_formatted_response_json(cls, robot_id, distance_to_goal, battery_level):
        return {'robotId': robot_id,
                'distanceToGoal': distance_to_goal,
                'batteryLevel': battery_level}

    @classmethod
    def get_formatted_error_response_json(cls):
        return cls.get_formatted_response_json(robot_id=cls._RESPONSE_JSON_ERROR_VALUE,
                                               distance_to_goal=cls._RESPONSE_JSON_ERROR_VALUE,
                                               battery_level=cls._RESPONSE_JSON_ERROR_VALUE)


class ClosestRobotRequestDispatcher(object):
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
        are_all_ints = (type(load_id) == int) and \
                       (type(x_coordinate) == int) and \
                       (type(y_coordinate) == int)
        return (are_all_ints) and (load_id >= 0)

    @classmethod
    def is_request_json_valid(cls, request_json):
        return cls._desired_keys_exist_in_json(request_json) and \
            cls._desired_value_ranges_exist_in_json(request_json)
