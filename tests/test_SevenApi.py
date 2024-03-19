from tests.BaseTest import BaseTest


class TestSevenApi(BaseTest):
    def test_instance(self) -> None:
        self.assertIsNotNone(self.client.apiKey)
