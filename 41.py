"""
Finds the largest 1-n digit prime pandigital 
Author: Juan Rios
"""

import math
import itertools

# Creates an array with prime numbers using the prime sieve
def is_prime(value):
    is_prime = True
    if value>2 and value%2==0:
        return False
    for i in range(3,int(math.sqrt(value))+1,2):
        if value%i==0:
            is_prime = False
    return is_prime

"""
Calculate permutations of n elements in k positions
"""
def elements_perm_k(elements,k):
    perm = []
    n = len(elements)
    for i in elements:
        perm.append(i)
    while (k>1):
        tmp = []
        for i in perm:
            for j in elements:
                if str(j) not in i:
                    tmp.append(i+str(j))
        k -= 1
        perm = tmp
    return perm

# Returns largest prime pandigital
def largest_pandigital_prime():
    perm7 = elements_perm_k('1234567',7)
    for i in range(len(perm7)-1, -1,-1):
        if (perm7[i][-1] in '2468'):
            continue
        if is_prime(int(perm7[i])):
            return perm7[i]
    return 'Pandigital prime not found'

    
if __name__ == "__main__":
    print('The largest 1-n pandigital that is prime is {0}'.format(largest_pandigital_prime())) 