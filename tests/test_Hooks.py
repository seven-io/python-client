from src.sms77api.classes.Hooks import HooksAction, HookEventType, HookRequestMethod
from tests.BaseTest import BaseTest


class TestHooks(BaseTest):
    hook_id = None

    def test_read(self) -> None:
        res = self.client.hooks(HooksAction.READ)

        self.assertIsInstance(res, dict)
        self.assertIsInstance(res['hooks'], list)
        self.assertIsInstance(res['success'], bool)

        for hook in res['hooks']:
            self.assertIsInstance(hook, dict)
            self.assertIsInstance(hook['created'], str)
            self.assertGreater(len(hook['created']), 0)
            self.assertIn(hook['event_type'], HookEventType.values())
            self.assertIsInstance(hook['id'], str)
            self.assertRegex(hook['id'], r'\d')
            self.assertIn(hook['request_method'], HookRequestMethod.values())
            self.assertIsInstance(hook['target_url'], str)
            self.assertGreater(len(hook['target_url']), 0)

    def test_subscribe(self) -> None:
        res = self.client.hooks(HooksAction.SUBSCRIBE, {
            'event_type': HookEventType.SMS_INBOUND.value,
            'request_method': HookRequestMethod.GET.value,
            'target_url': BaseTest.create_random_url(),
        })

        success = 'id' in res

        self.assertIsInstance(res, dict)

        if success:
            self.assertIsInstance(res['id'], int)
            self.assertGreater(res['id'], 0)
            self.hook_id = res['id']

        self.assertEqual(res['success'], success)

    def test_unsubscribe(self) -> None:
        if self.hook_id is None:
            return

        res = self.client.hooks(HooksAction.UNSUBSCRIBE, {'id': self.hook_id})

        self.assertIsInstance(res, dict)
        self.assertIsInstance(res['success'], bool)
