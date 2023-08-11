from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def values(cls):
        return list(map(lambda c: c.value, cls))
