# isPhoneNumber.py

def isPhoneNumber(text):
    """ Return True if text is valid American Phone Number """
    if len(text) != 12:
        return False
    if not text[:3].isdecimal():
        return False
    if text[3] != '-':
        return False
    if not text[4:7].isdecimal():
        return False
    if text[7] != '-':
        return False
    if not text[8:12].isdecimal():
        return False
    return True

if __name__ == '__main__':
    print('Is 415-555-4242 a phone number?')
    print(isPhoneNumber('415-555-4242'))
    print('Is Moshi-Moshi a phone number?')
    print(isPhoneNumber('Moshi-Moshi'))
    

    


    