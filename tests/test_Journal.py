from src.sms77api.classes.Journal import JournalType
from tests.BaseTest import BaseTest


class TestJournal(BaseTest):
    def base(self, _type, params={}, commons=True) -> list:
        entries = self.client.journal(_type, params)

        self.assertIsInstance(entries, list)

        for entry in entries:
            self.assertIsInstance(entry, dict)

            if commons:
                self.assertIsInstance(entry['from'], str)
                self.assertGreater(len(entry['from']), 0)

                self.assertIsInstance(entry['id'], str)
                self.assertGreater(len(entry['id']), 0)

                self.assertIsInstance(entry['price'], str)
                self.assertGreater(len(entry['price']), 0)

                self.assertIsInstance(entry['text'], str)

                self.assertIsInstance(entry['timestamp'], str)
                self.assertGreater(len(entry['timestamp']), 0)

                self.assertIsInstance(entry['to'], str)
                self.assertGreater(len(entry['to']), 0)

        return entries

    def test_inbound(self) -> None:
        for entry in self.base(JournalType.INBOUND, {}, False):
            self.assertIsInstance(entry['id'], str)
            self.assertIsInstance(entry['price'], str)
            self.assertIsInstance(entry['sender'], str)
            self.assertIsInstance(entry['system'], str)
            self.assertIsInstance(entry['text'], str)
            self.assertIsInstance(entry['time'], str)

    def test_outbound(self) -> None:
        for entry in self.base(JournalType.OUTBOUND):
            self.assertIsInstance(entry['connection'], str)
            self.assertGreater(len(entry['connection']), 0)

            if entry['dlr'] is None:
                self.assertIsNone(entry['dlr'])
            else:
                self.assertIsInstance(entry['dlr'], str)
                self.assertGreater(len(entry['dlr']), 0)

            if entry['dlr_timestamp'] is None:
                self.assertIsNone(entry['dlr_timestamp'])
            else:
                self.assertIsInstance(entry['dlr_timestamp'], str)
                self.assertGreater(len(entry['dlr_timestamp']), 0)

            if entry['foreign_id'] is None:
                self.assertIsNone(entry['foreign_id'])
            else:
                self.assertIsInstance(entry['foreign_id'], str)
                self.assertGreater(len(entry['foreign_id']), 0)

            if entry['label'] is None:
                self.assertIsNone(entry['label'])
            else:
                self.assertIsInstance(entry['label'], str)
                self.assertGreater(len(entry['label']), 0)

            if entry['latency'] is None:
                self.assertIsNone(entry['latency'])
            else:
                self.assertIsInstance(entry['latency'], str)
                self.assertGreater(len(entry['latency']), 0)

            if entry['mccmnc'] is None:
                self.assertIsNone(entry['mccmnc'])
            else:
                self.assertIsInstance(entry['mccmnc'], str)
                self.assertGreater(len(entry['mccmnc']), 0)

            self.assertIsInstance(entry['type'], str)
            self.assertGreater(len(entry['type']), 0)

    def test_replies(self) -> None:
        self.base(JournalType.REPLIES)

    def test_voice(self) -> None:
        for entry in self.base(JournalType.VOICE):
            self.assertIsInstance(entry['duration'], str)
            self.assertGreater(len(entry['duration']), 0)

            self.assertIsInstance(entry['error'], str)

            self.assertIsInstance(entry['status'], str)

            self.assertIsInstance(entry['xml'], bool)

    def test_voice_call(self) -> None:
        for entry in self.base(JournalType.VOICE_CALL, {}, False):
            self.assertIsInstance(entry['caller'], str)
            self.assertIsInstance(entry['id'], str)
            self.assertIsInstance(entry['system'], str)
            self.assertIsInstance(entry['time'], str)
