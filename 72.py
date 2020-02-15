"""
Finds the n/d value for d<=10*6, n<d to the left of 3/7
Author: Juan Rios
"""

import math
from utils import prime_factors
from itertools import combinations

def find_prime_factors(value,primes):
    factors = []
    tmp = value
    sqrt = int(math.sqrt(value))
    for p in primes:
        if p > sqrt or tmp==1:
            if tmp != 1:
                factors +=[tmp]
            break
        if tmp%p==0:
            factors += [p]
            tmp //= p
            while (tmp%p==0):
                tmp //= p
    return factors

def get_total_set(limit_value):
    primes = prime_factors(limit_value)
    primes_index = prime_factors(limit_value, False)
    counter = 0
    for d in range(2,limit_value+1):
        if primes_index[d]==1:
            counter += d-1
        else:
            tmp = d-1
            factors = find_prime_factors(d,primes)
            for e in range(0,len(factors)):
                variations = combinations(factors, r=e+1)
                for var in variations:
                    num = 1
                    for elem in var:
                        num *= elem
                    if (e+1)%2==0:
                        tmp += (d-1)//num
                    else: 
                        tmp -= (d-1)//num
            counter += tmp
    return counter

if __name__ == "__main__":
    limit_value = 10**6
    print('The number of elements in the set of reduced proper fractions for d<={0} is {1}'.format(limit_value, get_total_set(limit_value)))