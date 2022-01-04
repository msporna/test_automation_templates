import requests
from src.config import Config


class ApiManager:


    def _determine_host(self):
        return Config.api_host

    def make_get_request(self, endpoint, headers={}, timeout_seconds=45):
        endpoint = f"{self._determine_host()}{endpoint}"
        response = requests.get(endpoint, headers=headers, timeout=timeout_seconds)
        return response

    def make_post_request(self, endpoint, headers={}, payload={}, data={}, params={}, files={},
                          timeout_seconds=45, verify_ssl=False):
        endpoint = f"{self._determine_host()}{endpoint}"
        response = requests.post(endpoint, json=payload, data=data, headers=headers, files=files, params=params,
                                 timeout=timeout_seconds, verify=verify_ssl)
        return response