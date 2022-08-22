"""
Finds the largest prime factor of a number
Author: Juan Rios
"""
import math
import itertools

# Finds the prime factors of number
def prime_factors(number):
    primes = []
    # Loop through number 2, and every odd number below sqrt(number)
    for i in itertools.chain([2],range(3,math.floor(math.sqrt(number))+1,2)):
        # If number is divisible by i
        while(number%i==0):
            primes.append(i) # Add the number to the list of prime decomposition
            number /= i # Get the complement factor, where oldNumber = newNumber*i
        if number==1:
            # If number is 1, return primes list
            return primes
    return primes

if __name__ == "__main__":
    number = 600851475143
    print('The largest prime factor of the number {0} is {1}'.format(number, prime_factors(number)[-1]))
