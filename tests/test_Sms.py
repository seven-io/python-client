from tests.BaseTest import BaseTest


class TestSms(BaseTest):
    def test_sms(self) -> None:
        res = self.client.sms('+491771783130', 'HEY!!')
        self.assertEqual(res, '100')

        res = self.client.sms('+491771783130', 'HEY!!', {'return_msg_id': True})
        code, sid = res.splitlines()
        self.assertEqual(code, '100')
        self.assertIsInstance(sid, str)

        res = self.client.sms('+491771783130', 'HEY!!',
                              {'return_msg_id': True, 'details': True})
        lines = res.splitlines()
        self.assertEqual(lines[0], '100')
        self.assertIsInstance(lines[1], str)
        self.assertIsInstance(lines[2], str)
        self.assertIsInstance(lines[3], str)
        self.assertIsInstance(lines[4], str)
        self.assertIsInstance(lines[5], str)
        self.assertIsInstance(lines[6], str)
        self.assertIsInstance(lines[7], str)
        self.assertIsInstance(lines[8], str)
        self.assertIsInstance(lines[9], str)
        self.assertIsInstance(lines[10], str)

        # JSON
        res = self.client.sms('+491771783130', 'HEY!!', {'json': True, })
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
            self.assertIsInstance(message['sender'], str)
            self.assertIsInstance(message['recipient'], str)
            self.assertIsInstance(message['text'], str)
            self.assertIsInstance(message['encoding'], str)
            self.assertIsInstance(message['parts'], int)
            self.assertIsInstance(message['price'], (float, int))
            self.assertIsInstance(message['success'], bool)
            self.assertIn('error', message)
            self.assertIn('error_text', message)
