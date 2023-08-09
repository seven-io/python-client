from src.sms77api.classes.Pricing import PricingFormat
from tests.BaseTest import BaseTest


class TestPricing(BaseTest):
    def test_pricing(self) -> None:
        # CSV
        res = self.client.pricing(PricingFormat.CSV, 'fr')
        self.assertIsInstance(res, str)
        self.assertTrue(BaseTest.is_valid_delimiter(res))

        # JSON
        res = self.client.pricing(PricingFormat.JSON, 'de')
        self.assertIsInstance(res, dict)
        self.assertIsInstance(res['countCountries'], int)
        self.assertIsInstance(res['countNetworks'], int)
        self.assertIsInstance(res['countries'], list)

        country = BaseTest.first_list_item_fallback(res['countries'])
        if country:
            self.assertIsInstance(country['countryCode'], str)
            self.assertIsInstance(country['countryName'], str)
            self.assertIsInstance(country['countryPrefix'], str)
            self.assertIsInstance(country['networks'], list)
            network = BaseTest.first_list_item_fallback(country['networks'])
            if network:
                self.assertIsInstance(network['mcc'], str)
                self.assertIsInstance(network['mncs'], list)
                mnc = BaseTest.first_list_item_fallback(network['mncs'])
                if mnc:
                    self.assertIsInstance(mnc, str)
                self.assertIsInstance(network['networkName'], str)
                self.assertIsInstance(network['price'], float)
                self.assertIsInstance(network['features'], list)
                self.assertIsInstance(network['comment'], str)
