import requests
from src.sms77api.classes.Endpoint import Endpoint
from src.sms77api.classes.Method import Method
from src.sms77api.classes.ContactsAction import ContactsAction
from src.sms77api.classes.ContactsResponse import ContactsResponse

text_only_endpoints = [Endpoint.BALANCE.value]


def _expect_json(endpoint: str, params: dict):
    if endpoint in text_only_endpoints:
        return False
    if 'json' not in params:
        return False
    if params['json'] != (True | 1):
        return False
    return True


class Sms77api:
    apiKey = None
    sentWith = None
    baseUrl = 'https://gateway.sms77.io/api'

    def __init__(self, api_key: str, sent_with: str = 'Python'):
        self.apiKey = api_key
        self.sentWith = sent_with

    def balance(self, api_key: str = None):
        args = {}

        if api_key:
            args['p'] = api_key

        res = self._request(Method.GET, Endpoint.BALANCE, args)

        balance = float(res.text)

        if not isinstance(balance, float):
            raise ValueError('{} /{} {}'.format(Method.GET.value,
                                                Endpoint.BALANCE.value,
                                                res.text))

        return balance

    def contacts(self, action: ContactsAction, params: dict = {}):
        params['action'] = action.value
        method = Method.GET if 'read' == action else Method.POST
        expect_json = _expect_json(Endpoint.CONTACTS.value, params)
        res = self._request(method, Endpoint.CONTACTS, params)
        res = res.json() if expect_json else res.text
        is_dict = isinstance(res, dict)

        if is_dict:
            if 'id' in res:
                return int(res.id)
            if 'id' in params and int(
                    res['return']) in ContactsResponse.values():
                return int(params['id'])
            raise ValueError(
                '{} /{} {}'.format(method.value, Endpoint.CONTACTS.value, res))

        return res

    def _request(self, method: Method, endpoint: Endpoint, params={}):
        method = method.value
        endpoint = endpoint.value
        expect_json = _expect_json(endpoint, params)

        if not hasattr(params, 'p'):
            params['p'] = self.apiKey

        for key in params:
            if isinstance(params[key], bool):
                params[key] = 1 if params[key] is True else 0

        res = requests.request(method, self.baseUrl + '/' + endpoint,
                               **{'params': params})

        if res.status_code != 200:
            formatter = res.json() if expect_json else res.text
            raise ValueError('{}/ {} {}'.format(method, endpoint, formatter))

        return res

    def validate_for_voice(self, number: str, callback: str = None):
        res = self._request(Method.POST, Endpoint.VALIDATE_FOR_VOICE, locals()).json()

        return res
