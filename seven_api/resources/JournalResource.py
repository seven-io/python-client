from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Journal import JournalType
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class JournalResource(Resource):
    def outbound(self, params=None) -> list:
        return self.__get(JournalType.OUTBOUND, params)

    def inbound(self, params=None) -> list:
        return self.__get(JournalType.INBOUND, params)

    def voice(self, params=None) -> list:
        return self.__get(JournalType.VOICE, params)

    def replies(self, params=None) -> list:
        return self.__get(JournalType.REPLIES, params)

    def __get(self, journal_type: JournalType, params=None) -> list:
        if params is None: params = {}
        params['type'] = journal_type.value
        return self._client.request(Method.GET, Endpoint.JOURNAL, params).json()
