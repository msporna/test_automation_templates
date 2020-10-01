import requests


class ApiManager:

    def __init__(self, host):
        self.host = host

    def _build_complete_url(self, endpoint):
        return f"{self.host}/{endpoint}"

    def make_get_request(self, endpoint, headers={}):
        return requests.get(self._build_complete_url(endpoint), headers=headers)
