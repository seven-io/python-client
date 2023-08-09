import time

from src.sms77api.classes.Subaccounts import SubaccountsAction
from tests.BaseTest import BaseTest


class TestSubaccounts(BaseTest):
    def test_subaccounts_create_fail(self) -> None:
        action = SubaccountsAction.CREATE
        params = {
            'email': '',  # invalid email
            'name': '',  # invalid name
        }

        res = self.client.subaccounts(action, params)

        self.assertIsInstance(res, dict)

        self.assertIn('error', res)
        self.assertIsInstance(res['error'], str)

        self.assertIn('success', res)
        self.assertFalse(res['success'])

        self.assertNotIn('subaccount', res)

    def test_subaccounts_create_success(self) -> None:
        action = SubaccountsAction.CREATE
        timestamp = int(time.time())
        params = {
            'email': 'tom.test{}@seven.io'.format(timestamp),
            'name': 'Tom Test {}'.format(timestamp),
        }

        res = self.client.subaccounts(action, params)

        self.assertIsInstance(res, dict)

        self.assertIn('error', res)
        self.assertIsNone(res['error'])

        self.assertIn('success', res)
        self.assertTrue(res['success'])

        self.assertIn('subaccount', res)
        self.__assertSubaccount(res['subaccount'])

    def test_subaccounts_delete_fail(self) -> None:
        action = SubaccountsAction.DELETE
        params = {
            'id': 123456  # invalid ID
        }

        res = self.client.subaccounts(action, {**params})
        self.assertIsInstance(res, dict)
        self.assertFalse(res['success'])
        self.assertIsInstance(res['error'], str)

    def test_subaccounts_read(self) -> None:
        action = SubaccountsAction.READ

        res = self.client.subaccounts(action, {})
        self.assertIsInstance(res, list)

        for subaccount in res:
            self.assertIn('auto_topup', subaccount)
            self.assertIsInstance(subaccount['auto_topup'], dict)

            self.assertIn('amount', subaccount['auto_topup'])
            self.assertTrue(subaccount['auto_topup']['amount'] is None
                            or isinstance(subaccount['auto_topup']['amount'], int))

            self.assertIn('threshold', subaccount['auto_topup'])
            self.assertTrue(subaccount['auto_topup']['threshold'] is None
                            or isinstance(subaccount['auto_topup']['threshold'], int))

            self.assertIn('balance', subaccount)
            self.assertTrue(subaccount['balance'] is None or isinstance(subaccount['balance'], int))

            self.assertIn('company', subaccount)
            self.assertIsInstance(subaccount['company'], str)

            self.assertIn('contact', subaccount)
            self.assertIsInstance(subaccount['contact'], dict)
            self.assertIsInstance(subaccount['contact']['email'], str)
            self.assertIsInstance(subaccount['contact']['name'], str)

            self.assertIn('id', subaccount)
            self.assertIsInstance(subaccount['id'], int)

            self.assertIn('total_usage', subaccount)
            self.assertIsInstance(subaccount['total_usage'], int)

            self.assertIn('username', subaccount)
            self.assertTrue(subaccount['username'] is None or isinstance(subaccount['username'], str))

    def test_subaccounts_transfer_credits_fail(self) -> None:
        action = SubaccountsAction.TRANSFER_CREDITS
        params = {
            'amount': 0,  # invalid amount
            'id': '0',  # invalid id
        }

        res = self.client.subaccounts(action, params)
        self.assertFalse(res['success'])
        self.assertIsInstance(res['error'], str)

    def test_subaccounts_update_fail(self) -> None:
        action = SubaccountsAction.UPDATE
        params = {
            'amount': 0,  # invalid amount
            'id': '0',  # invalid id
            'threshold': -1,  # invalid threshold
        }

        res = self.client.subaccounts(action, params)
        self.assertFalse(res['success'])
        self.assertIsInstance(res['error'], str)

    def __assertSubaccount(self, subaccount):
        self.assertIn('auto_topup', subaccount)
        self.assertIsInstance(subaccount['auto_topup'], dict)

        self.assertIn('amount', subaccount['auto_topup'])
        self.assertTrue(subaccount['auto_topup']['amount'] is None
                        or isinstance(subaccount['auto_topup']['amount'], int))

        self.assertIn('threshold', subaccount['auto_topup'])
        self.assertTrue(subaccount['auto_topup']['threshold'] is None
                        or isinstance(subaccount['auto_topup']['threshold'], int))

        self.assertIn('balance', subaccount)
        self.assertIsInstance(subaccount['balance'], int)

        self.assertIn('company', subaccount)
        self.assertTrue(subaccount['company'] is None
                        or isinstance(subaccount['company'], str))

        self.assertIn('contact', subaccount)
        self.assertIsInstance(subaccount['contact'], dict)

        self.assertIn('email', subaccount['contact'])
        self.assertIsInstance(subaccount['contact']['email'], str)

        self.assertIn('name', subaccount['contact'])
        self.assertIsInstance(subaccount['contact']['name'], str)

        self.assertIn('id', subaccount)
        self.assertIsInstance(subaccount['id'], int)

        self.assertIn('total_usage', subaccount)
        self.assertIsInstance(subaccount['total_usage'], int)

        self.assertIn('username', subaccount)
        self.assertTrue(subaccount['username'] is None
                        or isinstance(subaccount['username'], str))
