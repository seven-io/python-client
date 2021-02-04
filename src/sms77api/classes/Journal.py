from sms77api.classes.ExtendedEnum import ExtendedEnum


class JournalType(ExtendedEnum):
    INBOUND = 'inbound'
    OUTBOUND = 'outbound'
    REPLIES = 'replies'
    VOICE = 'voice'
