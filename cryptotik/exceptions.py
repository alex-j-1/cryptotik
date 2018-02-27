
'''exceptions used by the library'''


class InvalidDelimiterError(Exception):
    '''Raised when invalid market-pair delimiter is used.'''
    pass


class InvalidBaseCurrencyError(Exception):
    '''Raised when base currency you are trying to use is not support by the exchange,
       or when you are giving this method a wrong input.'''
    pass
