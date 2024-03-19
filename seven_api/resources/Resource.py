from seven_api.SevenApi import SevenApi


class Resource:
    _client: SevenApi

    def __init__(self, client: SevenApi):
        self._client = client
