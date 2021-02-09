#! python3
# decimalToX.py

CONVERSION_TABLE = [str(i) for i in range(10)]
CONVERSION_TABLE += 'A B C D E F'.split()

def decToX(decimal, divisor):
    """
    Converts decimal to binary, octal or hexadecimal representation.
    The divisor dictates what type of representation that the decimal
    will be converted to:

    divisor = 2  -> binary
    divisor = 8  -> octal
    divisor = 16 -> hexadecimal
    """
    xRep = ''
    intPart = int(decimal)
    fractionPart = decimal - intPart

    while fractionPart > 0:
        result = fractionPart * divisor
        carry = int(result)
        xRep += CONVERSION_TABLE[carry]
        fractionPart = result - carry

    if xRep: 
        xRep = '.' + xRep

    while intPart > 0:
        xRep = CONVERSION_TABLE[intPart % divisor] + xRep
        intPart = intPart // divisor
    return xRep

if __name__ == '__main__':
    ex = 58.25
    print(decToX(decimal=ex, divisor=2))