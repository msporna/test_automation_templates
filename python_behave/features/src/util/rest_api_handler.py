import requests
from features.config import Config


class RestApiHandler:

    def _determine_host(self, api_name):
        if api_name == "versions":
            return Config.versions_api_host

    def make_get_request(self, api_name, endpoint, headers={}, timeout_seconds=45):
        endpoint = f"{self._determine_host(api_name)}{endpoint}"
        response = requests.get(endpoint, headers=headers, timeout=timeout_seconds)
        return response

    def make_post_request(self, api_name, endpoint, headers={}, payload={}, data={}, params={}, files={},
                          timeout_seconds=45, verify_ssl=False):
        endpoint = f"{self._determine_host(api_name)}{endpoint}"
        response = requests.post(endpoint, json=payload, data=data, headers=headers, files=files, params=params,
                                 timeout=timeout_seconds, verify=verify_ssl)
        return response
