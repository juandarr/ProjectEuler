"""
Finds the first fibonacci term with 1-9 pandigitals at the beginning and the end
Author: Juan Rios
"""
import math

def add_numbers(a,b):
    """
    Adds two numbers a,b given as strings
    """
    res = 0
    for i in range(8,-1,-1):
        val = a[i]+b[i]+res
        res = val//10
        a[i] = val%10
    return a

def pandigital_fibonnaci():
    phi = ( 1 + math.sqrt(5) ) / 2
    pan = [1,2,3,4,5,6,7,8,9]
    a = [0]*(8)+[1]
    b = [0]*(8)+[1]
    k = 2
    stored = []
    while True:
        tmp = b
        b = add_numbers(a,b)
        k += 1
        a = tmp
        if sorted(b)==pan:
            f = k* math.log10(phi) + math.log10(1/math.sqrt(5))
            f = int((pow(10, f-int(f) + 8)))
            if [int(i) for i in sorted(str(f))]==pan:
                return k


if __name__ == "__main__":
    print('The kth fibonacci term with 1-9 pandigitals at the beginning and end is {0}'.format(pandigital_fibonnaci())) 