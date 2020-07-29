import unittest
import os
from src.sms77api.classes.ContactsAction import ContactsAction
from src.sms77api.classes.ContactsResponse import ContactsResponse
import csv
from src.sms77api.Sms77api import Sms77api


class TestSms77api(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSms77api, self).__init__(*args, **kwargs)

        self.client = Sms77api(os.environ.get('SMS77_DUMMY_API_KEY'))

    def test_balance(self):
        res = self.client.balance()

        self.assertIsInstance(res, float)

    def test_contacts_del(self):
        action = ContactsAction.DEL
        params = {'id': 123456}

        # CSV
        res = self.client.contacts(action, params)
        self.assertEqual(int(res), ContactsResponse.CSV.value)

        # JSON
        res = self.client.contacts(action, {**params, 'json': 1})
        self.assertIsInstance(res, int)
        self.assertEqual(res, params['id'])

    def test_contacts_read(self):
        action = ContactsAction.READ

        # CSV
        res = self.client.contacts(action)
        if len(res):
            self.assertEqual(csv.Sniffer().sniff(res).delimiter, ';')
        else:
            self.assertEqual(res, '')

        # JSON
        self.assertIsInstance(self.client.contacts(action, {'json': 1}), list)

    def test_contacts_write(self):
        action = ContactsAction.WRITE
        params = {
            'email': 'wh@tev.er',
            'empfaenger': '+491771783130',
            'nick': 'Tom Tester',
        }

        # CREATE
        res = self.client.contacts(action, params)
        code, contact = res.splitlines()
        self.assertEqual(int(code), ContactsResponse.JSON.value)

        # EDIT
        contact = int(contact)
        res = self.client.contacts(action, {**params, id: contact})
        self.assertEqual(
            int(res.splitlines()[0]), ContactsResponse.JSON.value)

    def test_validate_for_voice(self):
        res = self.client.validate_for_voice(
            '+491771783130', 'sms77.io/my_dummy_callback.php')

        self.assertIsInstance(res, dict)

        self.assertTrue(res['success'])

    def test_voice(self):
        res = self.client.voice('+491771783130', 'HI2U!', False, 'Python')
        lines = res.splitlines()
        code = int(lines[0])
        vid = int(lines[1])
        cost = float(lines[2])

        self.assertEqual(len(lines), 3)
        self.assertIsInstance(code, int)
        self.assertIsInstance(vid, int)
        self.assertIsInstance(cost, float)

    def test_instance(self):
        self.assertIsNotNone(self.client.apiKey)


if __name__ == '__main__':
    unittest.main()
