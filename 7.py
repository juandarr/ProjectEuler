"""
Finds the nth prime number
Author: Juan Rios
"""
import math


# Finds prime factors until the index limit_index is met
def prime_factors(limit_index):
    primes = [2,3]
    n = 2
    current_value = 5
    while (n<limit_index):
        is_prime = True
        for prime in primes:
            if (math.sqrt(current_value)<prime):
                break
            elif (current_value%prime==0):
                is_prime = False
                break
        if (is_prime):
            primes.append(current_value)
            n += 1
        current_value += 2
    return primes[-1]

if __name__ == "__main__":
    index = 10001
    print('The prime number located at the {0} position is {1}'.format(index, prime_factors(index)))