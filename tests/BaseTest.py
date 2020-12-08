import unittest
import os
import csv
import uuid
from datetime import datetime
from src.sms77api.Sms77api import Sms77api


class BaseTest(unittest.TestCase):
    @staticmethod
    def is_valid_datetime(timestamp: str, formatting: str) -> bool:
        try:
            datetime.strptime(timestamp, formatting)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_delimiter(csv_: str) -> bool:
        return ';' == csv.Sniffer().sniff(csv_).delimiter

    @staticmethod
    def first_list_item_fallback(res: list) -> any:
        return next(iter(res), None)

    @staticmethod
    def create_random_url() -> str:
        return "http://my.tld/{0}".format(str(uuid.uuid4()))

    def __init__(self, *args, **kwargs) -> None:
        super(BaseTest, self).__init__(*args, **kwargs)

        self.client = Sms77api(os.environ.get('SMS77_DUMMY_API_KEY'))


if __name__ == '__main__':
    unittest.main()
