"""
Finds the largest prime factor of a number
Author: Juan Rios
"""
import math
import itertools

# Finds the prime factors of number
def prime_factors(number):
    primes = []
    for i in itertools.chain([2],range(3,math.floor(math.sqrt(number))+1,2)):
        while(number%i==0):
            primes.append(i)
            number /= i
        if number==1:
            return primes
    return primes

if __name__ == "__main__":
    number = 600851475143
    print('The largest prime factor of the number {0} is {1}'.format(number, prime_factors(number)[-1]))