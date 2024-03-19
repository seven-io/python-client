<img src="https://www.seven.io/wp-content/uploads/Logo.svg" width="250" />

# Python API Client

## Installation

Make sure you have [Python 3](https://www.python.org/downloads/) installed.

```shell script
pip3 install seven_api
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