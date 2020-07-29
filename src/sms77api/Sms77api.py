import requests
from src.sms77api.classes.Endpoint import Endpoint
from src.sms77api.classes.Method import Method
from src.sms77api.classes.ContactsAction import ContactsAction
from src.sms77api.classes.ContactsResponse import ContactsResponse

text_only_endpoints = [Endpoint.BALANCE.value, Endpoint.VOICE.value]


def expect_json(endpoint: str, params: dict):
    if endpoint in text_only_endpoints:
        return False
    if 'json' not in params:
        return False
    if params['json'] is not True and params['json'] != 1:
        return False
    return True


def local_params(locals_: dict):
    del locals_['self']
    return locals_


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

        res = self.__request(Method.GET, Endpoint.BALANCE, args)

        balance = float(res.text)

        if not isinstance(balance, float):
            raise ValueError('{} /{} {}'.format(Method.GET.value,
                                                Endpoint.BALANCE.value,
                                                res.text))

        return balance

    def contacts(self, action: ContactsAction, params: dict = {}):
        params['action'] = action.value
        method = Method.GET if 'read' == action else Method.POST
        res = self.__request(method, Endpoint.CONTACTS, params)
        res = res.json() if expect_json(Endpoint.CONTACTS.value, params) else res.text
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

    def validate_for_voice(self, number: str, callback: str = None):
        return self.__request(Method.POST, Endpoint.VALIDATE_FOR_VOICE,
                              local_params(locals())).json()

    def voice(self, to: str, text: str, xml: bool = False, sender: str = None):
        params = local_params(locals())
        params['from'] = sender
        del params['sender']

        return self.__request(Method.POST, Endpoint.VOICE, params).text

    def __request(self, method: Method, endpoint: Endpoint, params={}):
        method = method.value
        endpoint = endpoint.value

        if not hasattr(params, 'p'):
            params['p'] = self.apiKey

        for key in params:
            if isinstance(params[key], bool):
                params[key] = 1 if params[key] is True else 0

        url = '{}/{}'.format(self.baseUrl, endpoint)
        res = requests.request(method, url, **{'params': params})

        if res.status_code != 200:
            formatter = res.json() if expect_json(endpoint, params) else res.text
            raise ValueError('{} {} -> {}'.format(method, url, formatter))

        return res
