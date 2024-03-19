from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class BalanceResource(Resource):
    def retrieve(self) -> dict:
        return self._client.request(Method.GET, Endpoint.BALANCE)
