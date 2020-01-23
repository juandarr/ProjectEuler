"""
Finds the product of coefficients generation the longest sequence of prime numbers in n**2+a*n+b
Author: Juan Rios
"""

import math
import numpy as np

# Finds sum of prime factors below limit_value
def prime_factors(prime_dimension):
    values = np.ones(shape=(prime_dimension+1))
    values[0] = 0
    values[1] = 0
    values[4::2] = 0
    current_value = 3
    while (current_value<prime_dimension):
        if values[current_value]==1:
            values[2*current_value::current_value] = 0
        current_value += 2
    return values

def longest_sequence():
    primes = prime_factors(prime_dimension)
    max_primes = 0
    product = 0
    for a in range(-999,1000):
        for b in range(2,1001):
            if primes[b]==0:
                continue
            number_primes = 0
            for n in range(0,b):
                current_value = n**2+a*n+b 
                if current_value <= 1:
                    break
                else:
                    if primes[current_value]==1:
                        number_primes += 1
                    else:
                        break
            if number_primes > max_primes:
                max_primes = number_primes
                product = a*b
    return product


if __name__ == "__main__":
    prime_dimension = 100000
    print('The product of the coeffcients producing the longest sequence is {0}'.format(longest_sequence()))