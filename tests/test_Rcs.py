from tests.BaseTest import BaseTest


class TestRcs(BaseTest):
    def test_text(self) -> None:
        res = self.client.rcs.dispatch('+491716992343', 'Hey!')
        self.assertEqual(res['success'], '100')
        self.assertIsInstance(res['total_price'], (float, int))
        self.assertIsInstance(res['balance'], float)
        self.assertIsInstance(res['debug'], str)
        self.assertIsInstance(res['sms_type'], str)
        self.assertIsInstance(res['messages'], list)
        self.assertGreater(len(res['messages']), 0)
        message = BaseTest.first_list_item_fallback(res['messages'])
        if message:
            if 'true' == res['debug']:
                self.assertIsNone(message['id'])
            else:
                self.assertIsInstance(message['id'], int)

            self.assertEqual(message['channel'], 'RCS')
            self.assertIsInstance(message['sender'], str)
            self.assertIsInstance(message['recipient'], str)
            self.assertIsInstance(message['text'], str)
            self.assertIsInstance(message['encoding'], str)
            self.assertIsInstance(message['parts'], int)
            self.assertIsInstance(message['price'], (float, int))
            self.assertIsInstance(message['success'], bool)
            self.assertIn('error', message)
            self.assertIn('error_text', message)
