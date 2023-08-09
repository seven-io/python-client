from tests.BaseTest import BaseTest


class TestSms77api(BaseTest):
    def test_instance(self) -> None:
        self.assertIsNotNone(self.client.apiKey)
