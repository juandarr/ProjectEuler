"""
Finds the first n consecutive numbers to have n distinct prime factors each 
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
Return first n consecutive numbers with n distinct prime factors each
"""
def consecutive_with_distinct_primes(distinct):
    primes = prime_factors(10**6, True)
    i = 11
    valid = [] # Stores True when value i has n distinct primes
    while True:
        distinct_primes = set()
        tmp = i
        for div in primes:
            if div>math.sqrt(i):
                break
            while tmp%div==0:
                tmp //= div
                distinct_primes.add(div)
        if tmp>1:
            distinct_primes.add(tmp)
        if len(distinct_primes)==distinct:
            valid.append(True)
            if len(valid)==distinct:
                sol = []
                for c in range(distinct-1,-1,-1):
                    sol.append(i-c)
                return sol
        else:
            valid = []
        i += 1

if __name__ == "__main__":
    distinct = 4
    print('The first {0} consecutive numbers to have {0} prime factors each are {1}'.format(distinct,consecutive_with_distinct_primes(distinct))) 