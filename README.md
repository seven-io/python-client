![Sms77 Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "sms77")

# Python API Client

## Installation

Make sure you have [Python 3](https://www.python.org/downloads/) installed.

```shell script
pip3 install sms77api
```

### Methods

```python
def __init__(self, api_key: str, sent_with: str = 'Python'):
    pass


def analytics(self, params={}):
    pass


def balance(self, api_key: str = None):
    pass


def contacts(self, action: ContactsAction, params: dict = {}):
    pass


def hooks(self, action: HooksAction, params: dict = {}):
    pass


def journal(self, typ: JournalType, params: dict = {}):
    pass


def lookup(self, typ: LookupType, number: str, json: bool = False):
    pass


def pricing(self, format_: PricingFormat = PricingFormat.CSV, country: str = None):
    pass


def sms(self, to: str, text: str, params: dict = {}):
    pass


def status(self, msg_id: int):
    pass


def validate_for_voice(self, number: str, callback: str = None):
    pass


def voice(self, to: str, text: str, params: dict = {}):
    pass
```

#### Example

```python
from sms77api.Sms77api import Sms77api

client = Sms77api("InsertYourSuperSecretApiKeyFromSms77")
print(client.balance())
```

##### Support

Need help? Feel free to [contact us](https://www.sms77.io/en/company/contact/).

###### License

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)