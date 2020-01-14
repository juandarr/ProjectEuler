"""
Finds sum of all primes below limit_value using the prime sieve
Author: Juan Rios
"""
import math
import numpy as np

# Finds sum of prime factors below limit_value
def prime_factors_sum(limit_value):
    primes = [2]
    values = np.ones(shape=(1,limit_value))
    values[0,0] = 0
    values[0,1] = 0
    values[0,0::2] = 0

    sum_primes = 2
    current_value = 3
    while (current_value<limit_value):
        if values[0,current_value]==1:
            values[0,0::current_value] = 0
            sum_primes += current_value
        current_value += 2
    return sum_primes

if __name__ == "__main__":
    limit_value = 2000000
    print('The sum of primes below {0} is {1}'.format(limit_value, prime_factors_sum(limit_value)))