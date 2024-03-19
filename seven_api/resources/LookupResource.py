from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Lookup import LookupType
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class LookupResource(Resource):
    def cnam(self, params=None):
        return self.__post(LookupType.CNAM, params)

    def hlr(self, params=None):
        return self.__post(LookupType.HLR, params)

    def mnp(self, params=None):
        return self.__post(LookupType.MNP, params)

    def format(self, params=None):
        return self.__post(LookupType.FORMAT, params)

    def __post(self, type: LookupType, number: str):
        params = {
            'json': True,
            'number': number,
            'type': type,
        }
        return self._client.request(Method.GET, Endpoint.LOOKUP, params).json()
