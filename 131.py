"""
Finds the sum of primes below 10**6 with the property n**2+(n**2)*p=x**3
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

def primes_square_cube(limit_n):
    primes_index=prime_factors(limit_n+1, False)
    i = 0
    n = 2
    counter = 0
    while True:
        i = i+n
        tmp = i*3+1
        if tmp>10**6:
            break
        if primes_index[tmp]==1:
            counter+=1
        n += 2
    return counter

if __name__ == "__main__":
    limit_n = 10**6
    print('The sum of primes below 10**6 with the property n**2+(n**2)*p=x**3 is {0}'.format(primes_square_cube(limit_n)))