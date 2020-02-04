"""
Finds smallest prime of a family of primes obtained by replacing a set of digits for numbers from 0 to 9
Author: Juan Rios
"""

import math
from utils import prime_factors

"""
Returns smallest prime from the family of primes
"""
def prime_digit_replacements():
    primes_check = prime_factors(10**6, False)
    visited =[0]*(10**6+1)

    number = 56993
    visited[number] = 1

    largest = -float('inf')
    combination = ''
    smallest_prime = 0

    while True:
        value = str(number)
        combs = []
        
        for s in set(value[:-1]):
            string = s
            comb = ''
            for index in range(len(value)-1):
                if string==value[index]:
                    comb += str(index)
            combs.append(comb)

        for var in combs:
            prime_counter = 0
            
            for d in range(10):
                tmp = value
                for i in var:
                    tmp= tmp[:int(i)]+str(d)+tmp[int(i)+1:]
                if len(str(int(tmp)))==len(value):
                    if primes_check[int(tmp)]:
                        prime_counter += 1
            if largest < prime_counter:
                largest = prime_counter
                smallest_prime = number
                combination = var
            if prime_counter==8:
                return smallest_prime
        number += 2
        while not(primes_check[number]):
            number += 2
        
if __name__ == "__main__":
    print('The smallest prime with a family of 8 primes is {0}'.format(prime_digit_replacements())) 