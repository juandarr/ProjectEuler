"""
Finds the least value of n for which the first remainder first exceeds 10**10
Author: Juan Rios
"""
import math
from utils import prime_factors

def prime_remainders(limit_res):
    '''
    returns the least value of n for which the first remainder first exceeds 10**10
    '''
    primes = prime_factors(10**6)
    n=1
    for p in primes:
        if 2*n*p>limit_res and n%2!=0:
            return n
        n+=1

if __name__ == "__main__":
    limit_res = 10**10
    print('The least value of n for which the first remainder first exceeds {0} is {1}'.format(limit_res,prime_remainders(limit_res)))