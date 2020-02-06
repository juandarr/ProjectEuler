"""
Finds the length of the spiral at which the ratio primes and diagonal terms falls below 10%
Author: Juan Rios
"""

import math
from utils import prime_factors

"""
Return 1 if the number is prime, 0 otherwise
"""
def is_prime(number, primes):
    for p in primes:
        if p > math.sqrt(number):
            return 1
        if number%p==0:
            return 0
"""
Return the length of the spiral at which the ratio between primes and diagonals falls below 10%
"""
def ratio_tracker():
    primes_index = prime_factors(10**6,False)
    primes = prime_factors(10**6,True)
    print('Prime factors stored!')

    l = 7
    terms = 13
    prime_counter = 8
    corner_values =[31,37,43]
    while ((prime_counter/terms)> 0.1):
        l += 2
        terms += 4
        for index in range(len(corner_values)):
            corner_values[index] += (index+1)*2+4*(l-3)
            if corner_values[index]<10**6:
                if primes_index[corner_values[index]]:
                    prime_counter += 1
            else:
                prime_counter += is_prime(corner_values[index], primes)
    return l

if __name__ == "__main__":
    print('The lenght of the spiral where the ratio falls below 10% is {0}'.format(ratio_tracker()))