# stripRegex.py - A Regex version of the strip method.

import re

def strip(string, remove=' '):
    ''' Return the stripped version of a string. '''
    startREGEX = re.compile(f'^[{remove}]*')
    endREGEX = re.compile(f'[{remove}]*$')
    return endREGEX.sub('', startREGEX.sub('', string))


if __name__ == '__main__':
    # Test Cases
    stringOne = '  Hello, World  '
    print('Before: {} After: {}'.format(stringOne, strip(stringOne)))
    stringTwo = 'SpamSpamBaconSpamEggsSpamSpam'
    print('Before: {} After: {}'.format(stringTwo, strip(stringTwo, remove='ampS')))
