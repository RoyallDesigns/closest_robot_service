import requests


class JSONRetriever(object):

    def __init__(self, url_endpoint):
        self._url_endpoint = url_endpoint

    def get_json_data(self):
        try:
            response = requests.get(self._url_endpoint)
            return True, response.json()
        except requests.exceptions.RequestException as ex:
            return False, None
