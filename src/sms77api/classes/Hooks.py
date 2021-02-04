from sms77api.classes.ExtendedEnum import ExtendedEnum


class HooksAction(ExtendedEnum):
    READ = 'read'
    SUBSCRIBE = 'subscribe'
    UNSUBSCRIBE = 'unsubscribe'


class HookEventType(ExtendedEnum):
    SMS_STATUS = 'dlr'
    SMS_INBOUND = 'sms_mo'
    VOICE_STATUS = 'voice_status'


class HookRequestMethod(ExtendedEnum):
    GET = 'GET'
    POST = 'POST'
