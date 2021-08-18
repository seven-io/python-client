from tests.BaseTest import BaseTest


class TestVoice(BaseTest):
    def test_voice(self) -> None:
        res = self.client.voice('+491771783130', 'HI2U!',
                                {'xml': False, 'from': '+13134378004'})
        lines = res.splitlines()
        code = int(lines[0])
        vid = int(lines[1])
        cost = float(lines[2])

        self.assertEqual(len(lines), 3)
        self.assertIsInstance(code, int)
        self.assertIsInstance(vid, int)
        self.assertIsInstance(cost, float)
