# simplePhoneNumExtractor.py
# Extracts phone number on a text and prints it to the screen.

from isPhoneNumber import isPhoneNumber


def detectPhoneNumber(message):
    """ 
    Prints detected American phone-number on message. 
    """
    foundTotal = 0
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print(f'Phone Number Found: {chunk}')
            foundTotal += 1
    
    if foundTotal == 0:
        print('No American Phone Numbers Detected. :(')

if __name__ == '__main__':
    message = 'Call me @ 415-555-1011 tomorrow. 415-555-9999 is my office.'
    detectPhoneNumber(message)
