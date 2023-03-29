#!/bin/python3

import flask

# Internal Libraries
import json_helpers
import json_retriever
import calculators

SERVER_HOST = 'localhost'
SERVER_PORT = 5000
API_BASE_PATH = '/api/robots'
OK_RESPONSE_CODE = 200
BAD_REQUEST_RESPONSE_CODE = 400
UNSUPPORTED_MEDIA_TYPE_RESPONSE_CODE = 415
INTERNAL_SERVER_ERROR_CODE = 500
ROBOT_DATABASE_ENDPOINT_URL = 'https://60c8ed887dafc90017ffbd56.mockapi.io/robots'

g_flask_app = flask.Flask(__name__)
g_json_retriever = json_retriever.JSONRetriever(ROBOT_DATABASE_ENDPOINT_URL)


@g_flask_app.post('{}/closest'.format(API_BASE_PATH))
def determine_closest_robot():
    if flask.request.is_json:
        request_json = flask.request.get_json()
        if json_helpers.RequestJSONTransformer.is_request_json_valid(request_json):
            is_successful, robots_json = g_json_retriever.get_json_data()
            if is_successful:
                closest_robot = calculators.ClosestRobotCalculator.calculate_closest_robot_for_load_from_json_format(robots_json=robots_json,
                                                                                                                     load_json=request_json)
                if closest_robot:
                    response_json = json_helpers.ResponseJSONFormatter.get_formatted_response_json(robot_id=closest_robot.get_id(),
                                                                                                   distance_to_goal=closest_robot.get_distance_to_load(),
                                                                                                   battery_level=closest_robot.get_battery_level())
                else:
                    response_json = json_helpers.ResponseJSONFormatter.get_formatted_response_json(robot_id=None,
                                                                                                   distance_to_goal=None,
                                                                                                   battery_level=None)
                return (response_json, OK_RESPONSE_CODE)
            else:
                g_flask_app.logger.warning('Issue Connecting to Robot Database Endpoint.')
                return (json_helpers.ResponseJSONFormatter.get_formatted_error_response_json(),
                        INTERNAL_SERVER_ERROR_CODE)

        else:
            g_flask_app.logger.warning('Bad JSON Request. Improper Data or Formatting Supplied in Request.')
            return (json_helpers.ResponseJSONFormatter.get_formatted_error_response_json(),
                    BAD_REQUEST_RESPONSE_CODE)
    else:
        g_flask_app.logger.warning('Unsupported Media Type Supplied in Request.')
        return (json_helpers.ResponseJSONFormatter.get_formatted_error_response_json(),
                UNSUPPORTED_MEDIA_TYPE_RESPONSE_CODE)


def main():
    g_flask_app.run(host=SERVER_HOST,
                    port=SERVER_PORT)


if __name__ == '__main__':
    main()
