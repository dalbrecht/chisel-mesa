import requests
from typing import Mapping


class Client:
    def __init__(self, server_url: str):
        """

        :param server_url: str  URL for the ChiselMesa server
        """
        self._url = server_url

    def ping(self) -> Mapping:
        """

        :return:
        """
        return requests.get(self._url + "/ping/").json()
s