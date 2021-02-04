#! python3
# decimalToBinary.py

def decToBi(dec):
    ''' 
    This function uses subsequent division to solve the 
    Binary Representation of the given decimal.
    '''
    if dec == 1:
        return '1'
    else:
        q = dec // 2
        r = str(dec % 2)
        return decToBi(q) + r

if __name__ == '__main__':
    ex = 34
    print(decToBi(ex))