"""
Finds the number of elements between 1/3 and 1/2 for n<=12000
Author: Juan Rios
"""

import math
from utils import prime_factors

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

def find_counter_between(limit_value):
    primes = prime_factors(limit_value)
    primes_index = prime_factors(limit_value,False)
    lower = 1/3
    upper = 1/2
    counter = 0
    for i in range(2,limit_value+1):
        if primes_index[i]==1:
            counter += math.ceil(i/2)-math.floor(i/3)-1
        else:
            sequence = 0
            factors = find_prime_factors(i,primes)
            for s in range(math.ceil(i/3),math.floor(i/2)+1):
                ins = True
                for p in factors:
                    if s%p==0:
                        ins = False
                        break
                if ins:
                    sequence += 1
            counter += sequence
    return counter

if __name__ == "__main__":
    limit_value = 12000
    print('The number of elements between 1/3 and 1/2 in the sequence for n<={0} is {1}'.format(limit_value, find_counter_between(limit_value)))