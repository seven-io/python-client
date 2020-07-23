import requests


class Sms77api:
    apiKey = None
    sentWith = None
    baseUrl = 'https://gateway.sms77.io/api'

    def __init__(self, api_key, sent_with='Python'):
        self.apiKey = api_key
        self.sentWith = sent_with

    def balance(self):
        resp = self.request('GET', 'balance')

        balance = float(resp.text)

        if isinstance(balance, float) is not True:
            raise ValueError('GET /balance {}'.format(resp.text))

        return balance

    def request(self, method, endpoint, params={}):
        method = method.upper()
        isJsonResponse = 'balance' != endpoint and hasattr(params, 'json')
        kwargs = {}

        if len(params) != 0:
            payloadKey = 'params' if 'GET' == method else 'json'
            kwargs[payloadKey] = params

        res = requests.request(method, self.baseUrl + '/' + endpoint, **kwargs)

        if res.status_code != 200:
            formatter = res.json() if isJsonResponse else res.text
            raise ValueError(method + '/' + endpoint + '{}'.format(formatter))

        return res
