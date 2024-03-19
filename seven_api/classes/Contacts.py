from seven_api.classes.ExtendedEnum import ExtendedEnum


class ContactsAction(ExtendedEnum):
    READ = 'read'
    WRITE = 'write'
    DELETE = 'del'


class ContactsResponse(ExtendedEnum):
    CSV = 151
    JSON = 152
