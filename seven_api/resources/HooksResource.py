from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Hooks import HooksAction
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class HooksResource(Resource):
    def read(self) -> dict:
        return self._client.request(Method.GET, Endpoint.HOOKS, {'action': HooksAction.READ})

    def subscribe(self, params: dict) -> dict:
        params['action'] = HooksAction.SUBSCRIBE
        return self._client.request(Method.POST, Endpoint.HOOKS, params)

    def unsubscribe(self, hook_id: int) -> dict:
        params = {
            'action': HooksAction.UNSUBSCRIBE,
            'id': hook_id
        }
        return self._client.request(Method.POST, Endpoint.HOOKS, params)
