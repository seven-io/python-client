from src.sms77api.classes.Lookup import LookupType, MnpResponse
from tests.BaseTest import BaseTest


class TestLookup(BaseTest):
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
