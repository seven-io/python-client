import requests

from seven_api.classes.Endpoint import Endpoint
from seven_api.classes.Method import Method
from seven_api.resources.AnalyticsResource import AnalyticsResource
from seven_api.resources.BalanceResource import BalanceResource
from seven_api.resources.ContactsResource import ContactsResource
from seven_api.resources.HooksResource import HooksResource
from seven_api.resources.JournalResource import JournalResource
from seven_api.resources.LookupResource import LookupResource
from seven_api.resources.PricingResource import PricingResource
from seven_api.resources.RcsResource import RcsResource
from seven_api.resources.SmsResource import SmsResource
from seven_api.resources.SubaccountsResource import SubaccountsResource
from seven_api.resources.VoiceResource import VoiceResource


class SevenApi:
    analytics: AnalyticsResource
    apiKey: str
    balance: BalanceResource
    baseUrl = 'https://gateway.seven.io/api'
    contacts: ContactsResource
    hooks: HooksResource
    journal: JournalResource
    lookup: LookupResource
    pricing: PricingResource
    rcs: RcsResource
    sentWith: str
    sms: SmsResource
    subaccounts: SubaccountsResource
    voice: VoiceResource

    def __init__(self, api_key: str, sent_with: str = 'Python'):
        self.apiKey = api_key
        self.sentWith = sent_with

        self.analytics = AnalyticsResource(self)
        self.balance = BalanceResource(self)
        self.contacts = ContactsResource(self)
        self.hooks = HooksResource(self)
        self.journal = JournalResource(self)
        self.lookup = LookupResource(self)
        self.pricing = PricingResource(self)
        self.rcs = RcsResource(self)
        self.sms = SmsResource(self)
        self.subaccounts = SubaccountsResource(self)
        self.voice = VoiceResource(self)

    def request(self, method: Method, endpoint: Endpoint | str, params={}):
        method = method.value
        if not isinstance(endpoint, str):
            endpoint = endpoint.value

        for key in list(params):
            if isinstance(params[key], bool):
                if params[key]:
                    params[key] = 1
                else:
                    params.pop(key)

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'SentWith': self.sentWith,
            'X-Api-Key': self.apiKey
        }
        kwargs = {'headers': headers}
        if method is Method.GET:
            kwargs['params'] = params
        else:
            kwargs['json'] = params
        url = '{}/{}'.format(self.baseUrl, endpoint)
        res = requests.request(method, url, **kwargs)
        json = res.json()

        if res.status_code != 200 or not isinstance(json, dict) or not isinstance(json, list):
            raise ValueError('{} {} -> {}'.format(method, url, json))

        return json
