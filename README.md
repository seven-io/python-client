![Sms77 Logo](https://www.sms77.io/wp-content/uploads/2019/07/sms77-Logo-400x79.png "sms77")
# Sms77.io SMS Gateway API Client for Python

## Installation
```shell script
pip3 install sms77api
```

### Example
```python
from sms77api.Sms77api import Sms77api
client = Sms77api("InsertYourSuperSecretApiKeyFromSms77.Io!")
print(client.balance())
```