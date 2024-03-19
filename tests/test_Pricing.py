from seven_api.classes import PricingFormat
from tests.BaseTest import BaseTest


class TestPricing(BaseTest):

    def test_pricing_csv(self) -> None:
        res = self.client.pricing(PricingFormat.CSV, 'fr')
        self.assertIsInstance(res, str)
        self.assertTrue(BaseTest.is_valid_delimiter(res))

    def test_pricing_json(self) -> None:
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
                mncs = network['mncs']
                self.assertTrue(mncs is None or type(mncs) is list)
                if mncs is not None:
                    mnc = BaseTest.first_list_item_fallback(mncs)
                    if mnc:
                        self.assertIsInstance(mnc, str)
                network_name = network['networkName']
                self.assertTrue(network_name is None or type(network_name) is str)
                self.assertIsInstance(network['price'], float)
                self.assertIsInstance(network['features'], list)
                comment = network['comment']
                self.assertTrue(comment is None or type(comment) is str)
