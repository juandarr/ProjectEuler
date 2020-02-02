"""
Finds the prime below 1 million that is the sum of all consecutive primes below it
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
Returns first n consecutive numbers with n distinct prime factors each
"""
def prime_consecutive_sum(limit_value):
    primes  = prime_factors(limit_value, True)
    sum_primes =[]
    total = 0
    consecutives = -float('inf')
    max_prime = 0
    added = False
    for i in primes:
        total += i
        if total>10**6 and not(added):
            added = True
            limit_consecutives = len(sum_primes)
        sum_primes.append(total)
    print(len(sum_primes))
    for index in range(len(primes)-1, -1,-1):
        num = primes[index]
        if num < 990000:
            return max_prime
        starting_index = index-1
        while num<sum_primes[starting_index]:
            current_index = starting_index
            total = 0
            while starting_index-current_index+1<=limit_consecutives:
                total += primes[current_index]
                if total>num:
                    break
                if total==num:
                    if consecutives <starting_index-current_index+1:
                        consecutives = starting_index-current_index+1
                        max_prime = num
                        print(num,consecutives)
                current_index -= 1
            starting_index -= 1

if __name__ == "__main__":
    limit_value = 10**6
    print('The prime below {0} that is the sum of consecutive primes below it is {1}'.format(limit_value,prime_consecutive_sum(limit_value))) 