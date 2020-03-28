"""
Finds the sum of all primes below 100 thousand that will never be a factor of R(10**n)
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

def gcd(n,p,primes):
    factors_n={2:n,5:n}
    factors_p = decompose_primes(p,primes,True)
    val = 1
    for i in [2,5]:
        if i in factors_p:
            for n in range(min(factors_p[i],factors_n[i])):
                val *=i
    return val

def repunit_divisibility():
    primes = prime_factors(10**6)
    total = 2+3+5
    for i in primes[3:]:
        is_factor = False
        if  i<10**5:
                for n in range(1,50):
                    factor=gcd(n, i-1,primes)
                    if (10**factor)%i==1:
                        is_factor=True
                        break
                    if is_factor:
                        break
        else:
            return total
        if not(is_factor):
            total += i
    return total

if __name__ == "__main__":
    print('The sum of all primes below 100 thousand that will never be a factor of R(10**n) is {0}'.format(repunit_divisibility()))