from sms77api.classes.ExtendedEnum import ExtendedEnum


class LookupType(ExtendedEnum):
    CNAM = 'cnam'
    FORMAT = 'format'
    HLR = 'hlr'
    MNP = 'mnp'


LookupJsonTypes = [
    LookupType.FORMAT.value,
    LookupType.HLR.value,
    LookupType.CNAM.value,
]


class MnpResponse(ExtendedEnum):
    D1 = 'd1'
    D2 = 'd2'
    EPLUS = 'eplus'
    INT = 'int'
    NA = 'N/A'
    O2 = 'o2'
