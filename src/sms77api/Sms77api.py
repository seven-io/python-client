import requests

from sms77api.classes.Hooks import HooksAction
from sms77api.classes.Journal import JournalType
from sms77api.classes.Endpoint import Endpoint
from sms77api.classes.Method import Method
from sms77api.classes.Contacts import ContactsAction, ContactsResponse
from sms77api.classes.Lookup import LookupType, LookupJsonTypes
from sms77api.classes.Pricing import PricingFormat


def expect_json(endpoint: str, params: dict) -> bool:
    if endpoint in [Endpoint.BALANCE.value, Endpoint.VOICE.value]:
        return False
    if 'json' not in params:
        return False
    if params['json'] is not True and params['json'] != 1:
        return False
    return True


def local_params(locals_: dict) -> dict:
    del locals_['self']
    return locals_


class Sms77api:
    apiKey = None
    sentWith = None
    baseUrl = 'https://gateway.sms77.io/api'

    def __init__(self, api_key: str, sent_with: str = 'Python'):
        self.apiKey = api_key
        self.sentWith = sent_with

    def analytics(self, params={}):
        return self.__request(Method.GET, Endpoint.ANALYTICS, params).json()

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

        if isinstance(res, dict):
            if 'id' in res:
                return int(res['id'])
            if 'id' in params and int(res['return']) in ContactsResponse.values():
                return int(params['id'])

            raise ValueError(
                '{} /{} {}'.format(method.value, Endpoint.CONTACTS.value, res))

        return res

    def hooks(self, action: HooksAction, params: dict = {}):
        params['action'] = action.value
        method = Method.GET if action.READ == action else Method.POST
        res = self.__request(method, Endpoint.HOOKS, params)

        return res.json()

    def journal(self, _type: JournalType, params: dict = {}):
        params['type'] = _type.value
        res = self.__request(Method.GET, Endpoint.JOURNAL, params)

        return res.json()

    def lookup(self, type: LookupType, number: str, json: bool = False):
        type = type.value
        res = self.__request(Method.POST, Endpoint.LOOKUP, local_params(locals()))
        return res.json() if json or type in LookupJsonTypes else res.text

    def pricing(self, format: PricingFormat = PricingFormat.CSV, country: str = None):
        format = format.value
        res = self.__request(Method.GET, Endpoint.PRICING, local_params(locals()))
        return res.json() if PricingFormat.JSON.value == format else res.text

    def sms(self, to: str, text: str, params: dict = {}):
        params['to'] = to
        params['text'] = text
        res = self.__request(Method.POST, Endpoint.SMS, params)
        return res.json() \
            if 'json' in params \
               and (True is params['json'] or 1 == params['json']) else res.text

    def status(self, msg_id: int):
        return self.__request(Method.GET, Endpoint.STATUS, local_params(locals())).text

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

        for key in list(params):
            if isinstance(params[key], bool):
                if params[key]:
                    params[key] = 1
                else:
                    params.pop(key)

        url = '{}/{}'.format(self.baseUrl, endpoint)
        res = requests.request(method, url, **{'params': params})

        if res.status_code != 200:
            formatter = res.json() if expect_json(endpoint, params) else res.text
            raise ValueError('{} {} -> {}'.format(method, url, formatter))

        return res
