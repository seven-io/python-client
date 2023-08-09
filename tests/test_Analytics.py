from datetime import datetime, timedelta
from tests.BaseTest import BaseTest


class TestAnalytics(BaseTest):
    def test_analytics(self) -> None:
        today = datetime.today()
        start = (today - timedelta(days=90)).strftime('%Y-%m-%d')
        end = today.strftime('%Y-%m-%d')

        res = self.client.analytics(
            {'start': start, 'end': end, 'label': 'all', 'group_by': 'country'})

        self.assertIsInstance(res, list)

        msg = BaseTest.first_list_item_fallback(res)
        if msg:
            self.assertIsInstance(msg['country'], str)
            self.assertIsInstance(msg['hlr'], int)
            self.assertIsInstance(msg['inbound'], int)
            self.assertIsInstance(msg['mnp'], int)
            self.assertIsInstance(msg['sms'], int)
            self.assertIsInstance(msg['usage_eur'], float)
            self.assertIsInstance(msg['voice'], int)
