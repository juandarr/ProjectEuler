"""
Finds the sum of all truncable primes from left to right and right to left
Author: Juan Rios
"""
import math

# Creates an array with prime numbers using the prime sieve
def prime_factors(upper_limit):
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
    return values

# Finds the sum of truncable primes in both directions
def truncable_primes_sum():
    primes = prime_factors(upper_limit)
    truncable_primes = []
    i = 999999
    while (i>10):
        if primes[i]:
            str_number= str(i)
            if str_number[0] in '4689':
                str_number = str(int(str_number[0])-1)+''.join(['9' for i in range(len(str_number[1:]))])
                i = int(str_number)
                continue
            if str_number[-1]=='9':
                i-=2
                continue
            is_truncable = True
            for j in range(1,len(str_number)):
                tmp_l = str_number[j:]
                tmp_r = str_number[:-j]
                if not(primes[int(tmp_l)] and primes[int(tmp_r)]):
                    is_truncable = False
            if is_truncable:
                truncable_primes.append(i)
        i -= 2
    return sum(truncable_primes)

if __name__ == "__main__":
    upper_limit = 10**6
    print('The sum of all truncable primes from right to left and left to right is {0}'.format(truncable_primes_sum())) 