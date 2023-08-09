from src.sms77api.classes.Journal import JournalType
from src.sms77api.classes.Status import StatusMessage
from tests.BaseTest import BaseTest


class TestStatus(BaseTest):
    def test_status(self) -> None:
        msg = self.client.journal(JournalType.OUTBOUND)[0]['id']
        res = self.client.status(msg)
        self.assertIsInstance(res, str)

        status, timestamp = res.splitlines()
        self.assertIn(status, StatusMessage.values())
        self.assertTrue(BaseTest.is_valid_datetime(timestamp, "%Y-%m-%d %H:%M:%S.%f"))
