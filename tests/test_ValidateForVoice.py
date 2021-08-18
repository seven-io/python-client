from tests.BaseTest import BaseTest


class TestValidateForVoice(BaseTest):
    def test_validate_for_voice(self) -> None:
        res = self.client.validate_for_voice(
            '+491771783130', 'sms77.io/my_dummy_callback.php')

        self.assertIsInstance(res, dict)

        self.assertTrue(res['success'])
