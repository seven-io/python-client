from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class VoiceResource(Resource):
    def dispatch(self, params: dict) -> dict:
        params['json'] = True
        return self._client.request(Method.POST, Endpoint.VOICE, params).json()

    def validate(self, number: str, callback: str = None) -> dict:
        params = {
            'callback': callback,
            'number': number,
        }
        return self._client.request(Method.POST, Endpoint.VALIDATE_FOR_VOICE, params).json()
