from src.sms77api.classes.Contacts import ContactsAction, ContactsResponse
from tests.BaseTest import BaseTest


class TestContacts(BaseTest):
    def test_contacts_del(self) -> None:
        action = ContactsAction.DEL
        params = {'id': 123456}

        # CSV
        res = self.client.contacts(action, params)
        self.assertEqual(int(res), ContactsResponse.CSV.value)

        # JSON
        res = self.client.contacts(action, {**params, 'json': True})
        self.assertIsInstance(res, int)
        self.assertEqual(res, params['id'])

    def test_contacts_read(self) -> None:
        action = ContactsAction.READ

        # CSV
        res = self.client.contacts(action)
        if len(res):
            self.assertTrue(BaseTest.is_valid_delimiter(res))
        else:
            self.assertEqual(res, '')

        # JSON
        self.assertIsInstance(self.client.contacts(action, {'json': True}), list)

    def test_contacts_write(self) -> None:
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
        self.assertEqual(int(res.splitlines()[0]), ContactsResponse.JSON.value)
