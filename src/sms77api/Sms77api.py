import requests
from pprint import pprint


class Sms77api:
    apiKey = None
    sentWith = None
    baseUrl = 'https://gateway.sms77.io/api'

    def __init__(self, api_key, sent_with='Python'):
        self.apiKey = api_key
        self.sentWith = sent_with

    def balance(self, api_key=None):
        args = {}

        if api_key:
            args['p'] = api_key

        res = self.request('GET', 'balance', args)

        balance = float(res.text)

        if not isinstance(balance, float):
            raise ValueError('GET /balance {}'.format(res.text))

        return balance

    def request(self, method, endpoint, params={}):
        method = method.upper()
        is_json_res = 'balance' != endpoint and hasattr(params, 'json')
        url = self.baseUrl + '/' + endpoint
        payload_key = 'params'
        kwargs = {}

        if not hasattr(params, 'p'):
            params['p'] = self.apiKey

        if len(params) != 0:
            kwargs[payload_key] = params

        # pprint(kwargs)

        res = requests.request(method, url, **kwargs)

        if res.status_code != 200:
            formatter = res.json() if is_json_res else res.text
            raise ValueError(method + '/' + endpoint + '{}'.format(formatter))

        return res

    def validate_for_voice(self, number: str, callback: str = None):
        res = self.request('POST', 'validate_for_voice', locals()).json()

        return res
