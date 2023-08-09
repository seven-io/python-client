from tests.BaseTest import BaseTest


class TestBalance(BaseTest):
    def test_balance(self) -> None:
        res = self.client.balance()

        self.assertIsInstance(res, float)
