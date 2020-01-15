"""
Finds the first triangle number which has over five hundred divisors
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
    return primes

def triangle_number_factors(primes, limit):
    triangle_number = 1
    add = 2
    factors = 1
    while factors<=limit:
        factors = 1
        triangle_number += add
        add += 1
        num = triangle_number
        for prime in primes:
            repetition = 0
            while (num%prime ==0):
                num /= prime
                repetition += 1
            if repetition:
                factors *= (repetition+1)
            if num==1 or prime>math.sqrt(triangle_number):
                break
    return triangle_number   

if __name__ == "__main__":
    limit_index_primes = 500
    primes = prime_factors(limit_index_primes)
    limit = 500
    print('The first triangle number with over {0} factors is {1}'.format(limit,triangle_number_factors(primes,limit)))