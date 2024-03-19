from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource
from enum import Enum

Event = Enum('Event', ['IS_TYPING', 'READ'])


class RcsResource(Resource):
    def delete(self, id: int) -> dict:
        return self._client.request(Method.DELETE, f'{Endpoint.RCS.value}/messages/{id}').json()

    def dispatch(self, to: str, text: str, params=None) -> dict:
        if params is None:
            params = {}
        params['to'] = to
        params['text'] = text
        return self._client.request(Method.POST, f'{Endpoint.RCS.value}/messages', params).json()

    def event(self, to: str, event: Event, msg_id='') -> dict:
        params = {'event': event, 'to': to, 'msg_id': msg_id}
        return self._client.request(Method.POST, f'{Endpoint.RCS.value}/events', params).json()
