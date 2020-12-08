from src.sms77api.classes.ExtendedEnum import ExtendedEnum


class Endpoint(ExtendedEnum):
    ANALYTICS = 'analytics'
    BALANCE = 'balance'
    CONTACTS = 'contacts'
    HOOKS = 'hooks'
    LOOKUP = 'lookup'
    PRICING = 'pricing'
    SMS = 'sms'
    STATUS = 'status'
    VALIDATE_FOR_VOICE = 'validate_for_voice'
    VOICE = 'voice'
