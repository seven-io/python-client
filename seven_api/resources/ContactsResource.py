from seven_api.classes.Contacts import ContactsAction
from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.Resource import Resource


class ContactsResource(Resource):
    def delete(self, contact_id: int) -> dict:
        return self._client.request(Method.POST, Endpoint.CONTACTS, {
            'action': ContactsAction.DELETE,
            'id': contact_id
        })

    def read(self, contact_id: int = None) -> dict:
        params = {
            'action': ContactsAction.READ,
            'id': contact_id
        }
        return self._client.request(Method.GET, Endpoint.CONTACTS, params)

    def write(self, params: dict) -> dict:
        params['action'] = ContactsAction.WRITE
        return self._client.request(Method.POST, Endpoint.CONTACTS, params)
