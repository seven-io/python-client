![](https://www.seven.io/wp-content/uploads/Logo.svg "seven Logo")

# Python API Client

## Installation

Make sure you have [Python 3](https://www.python.org/downloads/) installed.

```shell script
pip3 install seven_api
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


def subaccounts(self, action: SubaccountsAction, params: dict = {}):
    pass


def validate_for_voice(self, number: str, callback: str = None):
    pass


def voice(self, to: str, text: str, params: dict = {}):
    pass
```

### Examples

#### Retrieve balance associated with given API key

```python
from seven_api.SevenApi import SevenApi

client = SevenApi("InsertYourSuperSecretApiKeyFromSeven")
print(client.balance())
```

#### Send an SMS and return a detailed JSON response

```python
from seven_api.SevenApi import SevenApi
import os

client = SevenApi(os.environ.get('SEVEN_API_KEY', 'FallbackValueIfMissing'))
print(client.sms('+49179999999999', 'Hi friend!', {'json': True}))
```

#### Support

Need help? Feel free to [contact us](https://www.seven.io/en/company/contact/).

###### License

[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)