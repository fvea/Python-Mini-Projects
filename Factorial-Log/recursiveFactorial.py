#!python3
# recursiveFactorial.py - solve for the factorial of a number.
# Tests also the debugging features of VS code. 

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    # Test case
    print(factorial(5))