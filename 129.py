"""
Finds the 2000th tile in the sequence of tiles being surrouded with 3 prime differences
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

def division(powers,primes):
    for p in primes:
        a = 1
        zeros = powers-1
        quot =''
        while a<p:
            a *= 10
            zeros -= 1
        while zeros>0:
            quot += str(a//p)
            a = a%p
            a *= 10
            zeros -=1
            while a<p  and zeros>0:
                a *= 10
                zeros -= 1
                quot += '0'
        if a>p:
            quot += str(a//p)
            a = a%p
        else:
            quot += str('0')
        a *= 10
        a += 1
        if a%p==0:
            return p,int(quot+str(a//p))
        else:
            return False

def repunit_divisibility(limit_n):
    exp = 1
    primes = prime_factors(10**6)
    factors = [11]
    exp +=1
    while 2**exp<10**6:
        unpack_primes = division(2**(exp-1),primes)
        if unpack_primes!=False:
            print(unpack_primes)
            break

if __name__ == "__main__":
    limit_n = 10
    print('The least value of n where the repunit length exceed {0} is {1}'.format(limit_n,repunit_divisibility(limit_n)))