from sms77api.classes.ExtendedEnum import ExtendedEnum


class StatusMessage(ExtendedEnum):
    DELIVERED = 'DELIVERED'
    NOTDELIVERED = 'NOTDELIVERED'
    BUFFERED = 'BUFFERED'
    TRANSMITTED = 'TRANSMITTED'
    ACCEPTED = 'ACCEPTED'
    EXPIRED = 'EXPIRED'
    REJECTED = 'REJECTED'
    FAILED = 'FAILED'
    UNKNOWN = 'UNKNOWN'
