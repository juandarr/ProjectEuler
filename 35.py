"""
Finds the number of circular primes below one million
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

"""
Number of circular primes below 10**6
"""
def circular_primes(upper_limit):
    primes = prime_factors(upper_limit)
    circular_primes = 5
    circular_dict = {2:1,3:1,5:1,7:1,11:1}
    i = 13
    while (i < upper_limit):
        num = str(i)
        if num[0] in '2468':
            num =str(int(num[0])+1)+num[1:]
            i = int(num)
            continue
        else:
            if primes[i]==1:
                n = len(num)
                circular = 1
                is_circular_prime = True
                if i not in circular_dict:
                    tmp = [num]
                    for j in range(n-1):
                        num = num[1:]+num[0]
                        if primes[int(num)]==1:
                            circular += 1
                            tmp.append(int(num))
                        else:
                            is_circular_prime= False
                            break
                    if is_circular_prime:
                            circular_primes += circular
                            for val in tmp:
                                circular_dict[val]=1
            i += 2
    return circular_primes


if __name__ == "__main__":
    upper_limit = 10**6
    print('The number of circular primes below {0} is {1}'.format(upper_limit,circular_primes(upper_limit))) 