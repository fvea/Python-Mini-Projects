#! python3
# decimalToBinary.py

def decToBi(dec):
    """
    Converts given decimal to its binary representaion.
    """

    intBiRep = ''                                   # Binary Rep. of integer part of the decimal.
    fBiRep = ''                                     # Binary Rep. of fractional part of the decimal.

    intDec = int(dec)
    fpart = dec - intDec
    if fpart != 0:                                  # Converts the fractional part of the decimal
        while fpart != 0:                           # to its equivalent binary representation.
            res = fpart * 2
            fBiRep += str(int(res))
            fpart = res - int(res)

    while intDec > 0:                               # Convert the integer part of the decimal to
        intBiRep = str(intDec % 2) + intBiRep       # its equivalent binary representation.
        intDec = intDec // 2
    
    if fBiRep:                                      
        return intBiRep + '.' + fBiRep
    return intBiRep


def decToOct(dec):
    """
    Converts given decimal to its octal representaion.
    """
    intOctRep = ''                                   # Octal Rep. of integer part of the decimal.
    fOctRep = ''                                     # Octal Rep. of fractional part of the decimal.

    intDec = int(dec)
    fpart = dec - intDec
    if fpart != 0:                                   # Converts the fractional part of the decimal
        while fpart != 0:                            # to its equivalent binary representation.
            res = fpart * 8
            fOctRep += str(int(res))
            fpart = res - int(res)

    while intDec > 0:                                # Convert the integer part of the decimal to
        intOctRep = str(intDec % 8) + intOctRep      # its equivalent octal representation.
        intDec = intDec // 8
    
    if fOctRep:  
        return intOctRep + '.' + fOctRep
    
    return intOctRep

if __name__ == '__main__':
    ex = 58.25
    print(decToOct(ex))