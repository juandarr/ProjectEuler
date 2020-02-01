"""
Finds the smallest odd composite that cannot be written as the sum of a prime and twice a square
Author: Juan Rios
"""

import math

"""
 Returns an array with prime numbers using the prime sieve
 This array can be in two forms:
    - An array of the primes themselves
    - Array of ones and zeros, where value is one where the index corresponds to a prime number
"""
def prime_factors(upper_limit, explicit_primes = True):
    values = [1]*(upper_limit+1)
    values[0] = 0
    values[1] = 0
    for i in range(4,upper_limit+1,2):
        values[i] = 0
    current_value = 3
    while (current_value<upper_limit):
        if values[current_value]==1:
            for i in range(2*current_value,upper_limit+1,current_value):
                values[i] = 0
        current_value += 2
    if not(explicit_primes):
        return values
    else:
        primes = []
        for i in range(len(values)):
            if values[i]==1:
                primes.append(i)
        return primes

"""
 Returns an array with twice a square values under upper limit
 This array can be in two forms:
    - An array of twice a square themselves
    - Array of ones and zeros, where value is one where the index corresponds to twice a square
"""
def twice_a_square(upper_limit, explicit_array = True):
    values = [0]*(upper_limit+1)
    i = 1
    while (2*i**2<=upper_limit):
        values[2*i**2] = 1
        i += 1 
    if not(explicit_array):
        return values
    else:
        twice_square = []
        for i in range(len(values)):
            if values[i]==1:
                twice_square.append(i)
        return twice_square
        

"""
Return the smallest odd composite that cannot be written as the sum of a prime and twice a square
"""
def smalles_odd_compositve():
    primes_array = prime_factors(10**6, False)
    primes = prime_factors(10**6, True)
    twice = twice_a_square(10**6, False)
    i = 9
    while True:
        condition = False
        if primes_array[i]==0:
            for p in primes:
                if (p<i):
                    j = i - p
                    if twice[j]==1:
                        condition = True
                        break
                else:
                    break
        else:
            i += 2
            continue
        if not(condition):
            return i
        i += 2

if __name__ == "__main__":
    print('The smallest odd composite that cannot be written as the sum of a prime and twice a square is {0}'.format(smalles_odd_compositve())) 