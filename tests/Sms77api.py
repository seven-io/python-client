import unittest
import os
from src.sms77api.Sms77api import Sms77api


class TestSms77api(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSms77api, self).__init__(*args, **kwargs)

        self.client = Sms77api(os.environ.get('SMS77_DUMMY_API_KEY'))

    def test_balance(self):
        res = self.client.balance()

        self.assertTrue(isinstance(res, float))

    def test_validate_for_voice(self):
        res = self.client.validate_for_voice('+491771783130', 'sms77.io/my_dummy_callback.php')

        self.assertTrue(isinstance(res, dict))

        self.assertTrue(res['success'])

    def test_instance(self):
        self.assertIsNotNone(self.client.apiKey)


if __name__ == '__main__':
    unittest.main()
