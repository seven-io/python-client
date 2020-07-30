from src.sms77api.classes.ExtendedEnum import ExtendedEnum


class Endpoint(ExtendedEnum):
    BALANCE = 'balance'
    CONTACTS = 'contacts'
    LOOKUP = 'lookup'
    VALIDATE_FOR_VOICE = 'validate_for_voice'
    VOICE = 'voice'
