import unittest
import os
import csv
from datetime import datetime, timedelta
from src.sms77api.classes.Contacts import ContactsAction, ContactsResponse
from src.sms77api.classes.Lookup import LookupType, MnpResponse
from src.sms77api.Sms77api import Sms77api
from src.sms77api.classes.Pricing import PricingFormat
from src.sms77api.classes.Status import StatusMessage


def is_valid_datetime(timestamp: str, format: str) -> bool:
    try:
        datetime.strptime(timestamp, format)
        return True
    except ValueError:
        return False


def is_valid_delimiter(csv_: str) -> bool:
    return ';' == csv.Sniffer().sniff(csv_).delimiter


def first_list_item_fallback(res: list) -> any:
    return next(iter(res), None)


class TestSms77api(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super(TestSms77api, self).__init__(*args, **kwargs)

        self.client = Sms77api(os.environ.get('SMS77_API_KEY'))

    def test_analytics(self) -> None:
        today = datetime.today()
        start = (today - timedelta(days=90)).strftime('%Y-%m-%d')
        end = today.strftime('%Y-%m-%d')

        res = self.client.analytics(
            {'start': start, 'end': end, 'label': 'all', 'group_by': 'country'})

        self.assertIsInstance(res, list)

        msg = first_list_item_fallback(res)
        if msg:
            self.assertIsInstance(msg['country'], str)
            self.assertIsInstance(msg['economy'], int)
            self.assertIsInstance(msg['direct'], int)
            self.assertIsInstance(msg['voice'], int)
            self.assertIsInstance(msg['hlr'], int)
            self.assertIsInstance(msg['mnp'], int)
            self.assertIsInstance(msg['inbound'], int)
            self.assertIsInstance(msg['usage_eur'], float)

    def test_balance(self) -> None:
        res = self.client.balance()

        self.assertIsInstance(res, float)

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
            self.assertTrue(is_valid_delimiter(res))
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

    def test_lookup_cnam(self) -> None:
        res = self.client.lookup(LookupType.CNAM, '+491771783130')

        self.assertIsInstance(res, dict)
        self.assertIsInstance(res['success'], str)
        self.assertIsInstance(res['code'], str)
        self.assertIsInstance(res['number'], str)
        self.assertIsInstance(res['name'], str)

    def test_lookup_format(self) -> None:
        res = self.client.lookup(LookupType.FORMAT, '+491771783130')

        self.assertIsInstance(res, dict)
        self.assertTrue(res['success'])
        self.assertIsInstance(res['national'], str)
        self.assertIsInstance(res['international'], str)
        self.assertIsInstance(res['international_formatted'], str)
        self.assertIsInstance(res['country_name'], str)
        self.assertIsInstance(res['country_code'], str)
        self.assertIsInstance(res['country_iso'], str)
        self.assertIsInstance(res['carrier'], str)
        self.assertIsInstance(res['network_type'], str)

    def test_lookup_hlr(self) -> None:
        def is_valid_carrier(carrier: dict):
            valid = isinstance(carrier['network_code'], str)
            valid = isinstance(carrier['name'], str) if valid else False
            valid = isinstance(carrier['country'], str) if valid else False
            valid = isinstance(carrier['network_type'], str) if valid else False

            return valid

        res = self.client.lookup(LookupType.HLR, '+491771783130')

        self.assertIsInstance(res, dict)
        self.assertIsInstance(res['status'], bool)
        self.assertIsInstance(res['status_message'], str)
        self.assertIsInstance(res['lookup_outcome'], bool)
        self.assertIsInstance(res['lookup_outcome_message'], str)
        self.assertIsInstance(res['international_format_number'], str)
        self.assertIsInstance(res['international_formatted'], str)
        self.assertIsInstance(res['national_format_number'], str)
        self.assertIsInstance(res['country_code'], str)
        self.assertIsInstance(res['country_name'], str)
        self.assertIsInstance(res['country_prefix'], str)
        self.assertIsInstance(res['current_carrier'], dict)
        self.assertIsInstance(res['original_carrier'], dict)
        self.assertIsInstance(res['valid_number'], str)
        self.assertIsInstance(res['reachable'], str)
        self.assertIsInstance(res['ported'], str)
        self.assertIsInstance(res['roaming'], str)
        self.assertIsInstance(res['gsm_code'], str)
        self.assertIsInstance(res['gsm_message'], str)
        self.assertTrue(is_valid_carrier(res['current_carrier']))
        self.assertTrue(is_valid_carrier(res['original_carrier']))

    def test_lookup_mnp(self) -> None:
        res = self.client.lookup(LookupType.MNP, '+491771783130')
        self.assertIsInstance(res, str)
        self.assertIn(res, MnpResponse.values())

        # JSON
        res = self.client.lookup(LookupType.MNP, '+491771783130', True)
        self.assertIsInstance(res, dict)

        self.assertTrue(res['success'])
        self.assertEqual(res['code'], 100)
        self.assertIsInstance(res['price'], float)
        self.assertIsInstance(res['mnp'], dict)

        self.assertIsInstance(res['mnp']['country'], str)
        self.assertIsInstance(res['mnp']['number'], str)
        self.assertIsInstance(res['mnp']['national_format'], str)
        self.assertIsInstance(res['mnp']['international_formatted'], str)
        self.assertIsInstance(res['mnp']['network'], str)
        self.assertIsInstance(res['mnp']['mccmnc'], str)
        self.assertIsInstance(res['mnp']['isPorted'], bool)

    def test_pricing(self) -> None:
        # CSV
        res = self.client.pricing(PricingFormat.CSV, 'fr')
        self.assertIsInstance(res, str)
        self.assertTrue(is_valid_delimiter(res))

        # JSON
        res = self.client.pricing(PricingFormat.JSON, 'de')
        self.assertIsInstance(res, dict)
        self.assertIsInstance(res['countCountries'], int)
        self.assertIsInstance(res['countNetworks'], int)
        self.assertIsInstance(res['countries'], list)

        country = first_list_item_fallback(res['countries'])
        if country:
            self.assertIsInstance(country['countryCode'], str)
            self.assertIsInstance(country['countryName'], str)
            self.assertIsInstance(country['countryPrefix'], str)
            self.assertIsInstance(country['networks'], list)
            network = first_list_item_fallback(country['networks'])
            if network:
                self.assertIsInstance(network['mcc'], str)
                self.assertIsInstance(network['mncs'], list)
                mnc = first_list_item_fallback(network['mncs'])
                if mnc:
                    self.assertIsInstance(mnc, str)
                self.assertIsInstance(network['networkName'], str)
                self.assertIsInstance(network['price'], float)
                self.assertIsInstance(network['features'], list)
                self.assertIsInstance(network['comment'], str)

    def test_status(self) -> None:
        res = self.client.status(77127422642)
        self.assertIsInstance(res, str)

        status, timestamp = res.splitlines()
        self.assertIn(status, StatusMessage.values())
        self.assertTrue(is_valid_datetime(timestamp, "%Y-%m-%d %H:%M:%S.%f"))

    def test_validate_for_voice(self) -> None:
        res = self.client.validate_for_voice(
            '+491771783130', 'sms77.io/my_dummy_callback.php')

        self.assertIsInstance(res, dict)

        self.assertTrue(res['success'])

    def test_voice(self) -> None:
        res = self.client.voice('+491771783130', 'HI2U!', False, 'Python')
        lines = res.splitlines()
        code = int(lines[0])
        vid = int(lines[1])
        cost = float(lines[2])

        self.assertEqual(len(lines), 3)
        self.assertIsInstance(code, int)
        self.assertIsInstance(vid, int)
        self.assertIsInstance(cost, float)

    def test_instance(self) -> None:
        self.assertIsNotNone(self.client.apiKey)


if __name__ == '__main__':
    unittest.main()
