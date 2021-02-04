from sms77api.classes.ExtendedEnum import ExtendedEnum


class ContactsAction(ExtendedEnum):
    READ = 'read'
    WRITE = 'write'
    DEL = 'del'


class ContactsResponse(ExtendedEnum):
    CSV = 151
    JSON = 152
