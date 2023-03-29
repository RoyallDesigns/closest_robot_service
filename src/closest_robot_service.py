#!/bin/python3

import flask

# Internal Libraries
import json_helpers

SERVER_HOST = 'localhost'
SERVER_PORT = 5000
API_BASE_PATH = '/api/robots'
OK_RESPONSE_CODE = 200
BAD_REQUEST_RESPONSE_CODE = 400
UNSUPPORTED_MEDIA_TYPE_RESPONSE_CODE = 415

g_flask_app = flask.Flask(__name__)


@g_flask_app.post('{}/closest'.format(API_BASE_PATH))
def determine_closest_robot():
    if flask.request.is_json:
        request_json = flask.request.get_json()
        if json_helpers.RequestJSONTransformer.is_request_json_valid(request_json):
            load = json_helpers.RequestJSONTransformer.create_load_from_request_json(request_json)
            return (json_helpers.ResponseJSONFormatter.get_formatted_response_json(robot_id=0,
                                                                                   distance_to_goal=0,
                                                                                   battery_level=0),
                    OK_RESPONSE_CODE)
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
