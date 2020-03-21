"""
Finds the 10000th element of the sorted list by value and then by n of radicals (product of primes of every number)
Author: Juan Rios
"""
import math
from utils import prime_factors,decompose_primes

def radicals_finder(limit_i):
    '''
    returns the 10000th element of the sorted list by value and then by n of radicals
    '''
    primes = prime_factors(1000)
    radicals = [(1,1)]
    for n in range(2,limit_i+1):
        dec = decompose_primes(n,primes,True) 
        rad = 1
        for i in dec:
            rad *= i
        radicals.append((n,rad))
    rad_sorted = sorted(radicals, key = lambda x: (x[1],x[0]))
    return rad_sorted[9999][0]
        

if __name__ == "__main__":
    limit_i = 10**5
    print('the 10000th element of the sorted list by value and then by n of radicals is {0}'.format(radicals_finder(limit_i)))