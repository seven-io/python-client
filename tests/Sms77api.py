import unittest
import os
from src.sms77api.Sms77api import Sms77api


class TestSms77api(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSms77api, self).__init__(*args, **kwargs)

        apiKey = os.environ.get('SMS77_DUMMY_API_KEY')
        self.client = Sms77api(apiKey)

    def test_instance(self):
        self.assertIsNotNone(self.client.apiKey)

    def test_balance(self):
        result = self.client.balance()

        boolean = isinstance(result, float)
        self.assertTrue(boolean)


if __name__ == '__main__':
    unittest.main()
