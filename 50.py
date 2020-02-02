"""
Finds the prime below 1 million that is the sum of all consecutive primes below it
Author: Juan Rios
"""

import math
from utils import prime_factors

"""
Returns first n consecutive numbers with n distinct prime factors each
"""
def prime_consecutive_sum(limit_value):
    primes  = prime_factors(limit_value, True)

    consecutives = -float('inf')
    max_prime = 0

    for index in range(len(primes)-1, -1,-1):
        num = primes[index]
        if num < 990000:
            return max_prime
        starting_index = 0
        while True:
            current_index = starting_index
            if index-starting_index+1<consecutives or starting_index==index:
                break
            total = 0
            while True:
                total += primes[current_index]
                if total>num or current_index==index:
                    break
                if total==num:
                    if consecutives < current_index-starting_index+1:
                        consecutives = current_index-starting_index+1
                        max_prime = num
                        print(num,consecutives)
                    break
                current_index += 1
            starting_index += 1

if __name__ == "__main__":
    limit_value = 10**6
    print('The prime below {0} that is the sum of consecutive primes below it is {1}'.format(limit_value,prime_consecutive_sum(limit_value))) 