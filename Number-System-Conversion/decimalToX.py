#! python3
# decimalToBinary.py

def decToBi(dec, _havefPart=False):
    ''' 
    This function uses sucessive division to return the 
    Binary Representation of the given decimal.
    '''
    # Checks wether the given dec have fractional part.
    fractionPart = dec - int(dec)
    if fractionPart != 0 and not _havefPart:
        return decToBi(int(dec)) + '.' + decToBi(fractionPart, _havefPart=True)

    if _havefPart: 
        res = dec * 2
        fPart = res - int(res)
        if fPart == 0:
            return '1'
        else:
            return str(int(res)) + decToBi(fPart, _havefPart=True)
    else:
        if dec < 2:
            return '1'
        else:
            q = dec // 2
            r = dec % 2
            return decToBi(q) + str(r)

def decToOct(dec, _havefPart=False):
    """
    This function uses sucessive division to return the 
    Octal Representation of the given decimal.
    """
    # Checks wether the given dec have fractional part.
    fractionPart = dec - int(dec)
    if fractionPart != 0 and not _havefPart:
        return decToOct(int(dec)) + '.' + decToOct(fractionPart, _havefPart=True)

    if _havefPart:    
        res = dec * 8
        fPart = res - int(res)
        if fPart == 0:
            return str(int(res))
        else:
            return str(int(res)) + decToOct(fPart, _havefPart=True)
    else:
        if dec < 8:
            return str(dec)
        else:
            q = dec // 8
            r = dec % 8
            return decToOct(q) + str(r)

def decToBiITR(dec):

    intBiRep = ''       # Binary Rep. of integer part of the decimal.
    fBiRep = ''         # Binary Rep. of fractional part of the decimal.

    intDec = int(dec)
    fpart = dec - intDec
    if fpart != 0:
        while fpart != 0:
            res = fpart * 2
            fBiRep += str(int(res))
            fpart = res - int(res)

    while intDec > 0:
        intBiRep = str(intDec % 2) + intBiRep
        intDec = intDec // 2
    
    if fBiRep:
        return intBiRep + '.' + fBiRep
    return intBiRep
    



if __name__ == '__main__':
    ex = 58.25
    print(decToBiITR(ex))