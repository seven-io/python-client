from sms77api.classes.ExtendedEnum import ExtendedEnum


class HooksAction(ExtendedEnum):
    READ = 'read'
    SUBSCRIBE = 'subscribe'
    UNSUBSCRIBE = 'unsubscribe'


class HookEventType(ExtendedEnum):
    ALL = 'all'
    SMS_STATUS = 'dlr'
    SMS_INBOUND = 'sms_mo'
    TRACKING = 'tracking'
    VOICE_CALL = 'voice_call'
    VOICE_STATUS = 'voice_status'


class HookRequestMethod(ExtendedEnum):
    GET = 'GET'
    JSON = 'JSON'
    POST = 'POST'
