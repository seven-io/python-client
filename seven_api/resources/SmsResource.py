from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class SmsResource(Resource):
    def delete(self, ids: list) -> dict:
        return self._client.request(Method.DELETE, Endpoint.SMS, {'ids': ids}).json()

    def dispatch(self, params: dict) -> dict:
        params['json'] = True
        return self._client.request(Method.POST, Endpoint.SMS, params).json()

    def status(self, ids: list) -> dict:
        return self._client.request(Method.GET, Endpoint.STATUS, {'msg_id': ids, 'json': True}).json()
