#! python3
# strongPasswd.py
#   - contains isStrong(passwd) function that checks wether the
#     given passwd is strong.
#
# Criteria used for a strong password.
# 1. Atleast 8 chars long.
# 2. Contains both uppercase and lowercase letters.
# 3. Contains atleast 1 digit.

import re

def isStrong(passwd):
    ''' Returns True if the password is strong. '''
    
    # REGEX patterns that the given password must followed.
    digitsREGEX = re.compile(r'\d+')
    lowercaseREGEX = re.compile(r'[a-z]+')
    uppercaseREGEX = re.compile(r'[A-Z]+')
    lenREGEX = re.compile(r'.{8,}')

    if lenREGEX.search(passwd) and lowercaseREGEX.search(passwd) and \
        uppercaseREGEX.search(passwd) and digitsREGEX.search(passwd):
        return True
    else:
        return False

if __name__ == '__main__':
    passwordOne = '9eFS463B'
    print(isStrong(passwordOne)) # prints true
    passwordTwo = 'fveataba3'
    print(isStrong(passwordTwo)) # prints false