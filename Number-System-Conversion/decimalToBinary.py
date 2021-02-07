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
        # The fractional part also need to be converted.
        # The binary rep. for int part is seperated in
        # binary rep. of fractional part with '.'
        return decToBi(int(dec)) + '.' + decToBi(fractionPart, _havefPart=True)

    if _havefPart:
        # Case if the function is converting the fractional 
        # part to its binary rep.      
        res = dec * 2
        fPart = res - int(res)
        if fPart == 0:
            return '1'
        else:
            return str(int(res)) + decToBi(fPart, _havefPart=True)
    else:
        # Case if the function is converting the integer part
        # to its binary rep.
        if dec == 1:
            return '1'
        else:
            q = dec // 2
            r = str(dec % 2)
            return decToBi(q) + r

if __name__ == '__main__':
    ex = 21.1
    print(decToBi(ex))