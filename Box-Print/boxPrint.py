#! python3
# boxPrint.py - contains the function boxPrint() that
# takes a character, a width, and a height, and uses the 
# character to make a little picture of a box with that 
# width and height. This box shape is printed to the screen.

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be grater than 2.')

    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)

