#!/bin/python3

import flask

# Internal Libraries
import helpers

SERVER_HOST = 'localhost'
SERVER_PORT = 5000
API_BASE_PATH = '/api/robots'
OK_RESPONSE_CODE = 200
UNSUPPORTED_MEDIA_TYPE_RESPONSE_CODE = 415

g_flask_app = flask.Flask(__name__)


@g_flask_app.post('{}/closest'.format(API_BASE_PATH))
def determine_closest_robot():
    if flask.request.is_json and \
       helpers.ClosestRobotRequestDispatcher.is_request_json_valid(flask.request.get_json()):
        return (helpers.ResponseJSONFormatter.get_formatted_response_json(robot_id=0,
                                                                          distance_to_goal=0,
                                                                          battery_level=0),
                OK_RESPONSE_CODE)
    g_flask_app.logger.warning('Unsupported Data Supplied in JSON Request.')
    return (helpers.ResponseJSONFormatter.get_formatted_error_response_json(),
            UNSUPPORTED_MEDIA_TYPE_RESPONSE_CODE)


def main():
    g_flask_app.run(host=SERVER_HOST,
                    port=SERVER_PORT)


if __name__ == '__main__':
    main()
