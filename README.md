![Sms77 Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "sms77")
# Official Python API Client for the Sms77.io SMS Gateway


## Installation
```shell script
pip3 install sms77api
```

### Methods
```python
def __init__(self, api_key: str, sent_with: str = 'Python'):
def analytics(self, params={}):
def balance(self, api_key: str = None):
def contacts(self, action: ContactsAction, params: dict = {}):
def hooks(self, action: HooksAction, params: dict = {}):
def journal(self, typ: JournalType, params: dict = {}):
def lookup(self, typ: LookupType, number: str, json: bool = False):
def pricing(self, format_: PricingFormat = PricingFormat.CSV, country: str = None):
def sms(self, to: str, text: str, params: dict = {}):
def status(self, msg_id: int):
def validate_for_voice(self, number: str, callback: str = None):
def voice(self, to: str, text: str, params: dict = {}):
```

#### Example
```python
from sms77api.Sms77api import Sms77api
client = Sms77api("InsertYourSuperSecretApiKeyFromSms77.Io!")
print(client.balance())
```


##### Support
Need help? Feel free to [contact us](https://www.sms77.io/en/company/contact/).


###### License

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)