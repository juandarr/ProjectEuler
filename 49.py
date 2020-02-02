"""
Finds the three term in an arithmetic sequence of 4-digit permutations
Author: Juan Rios
"""

import math
from utils import prime_factors

"""
Calculate permutations of n elements in k positions
"""
def elements_perm_k(elements,k):
    perms = []
    n = len(elements)
    for i in range(len(elements)):
        perms.append(str(i))
    while (k>1):
        tmp = []
        for i in perms:
            for j in range(n):
                if str(j) not in i:
                    tmp.append(i+str(j))
        k -= 1
        perms = tmp
    variations =[]
    for perm in perms:
        variation = elements[int(perm[0])]+elements[int(perm[1])]+elements[int(perm[2])]+elements[int(perm[3])]
        if variation not in variations:
            variations.append(variation)
    return sorted(variations)

"""
Returns first n consecutive numbers with n distinct prime factors each
"""
def arithmetic_sequence():
    primes = prime_factors(10**6, False)
    perm_used = [0]*10000
    for value in range(1001,9987):
        perm4 = elements_perm_k(str(value),4)
        if perm_used[int(perm4[0])]==0:
            for a in range(0,len(perm4)-2):
                if primes[int(perm4[a])] and int(perm4[a])>1000:
                    for b in range(a+1,len(perm4)-1):
                        if primes[int(perm4[b])] and int(perm4[b])>1000:
                            d2 = int(perm4[b])-int(perm4[a])
                            for c in range(b+1,len(perm4)):
                                if primes[int(perm4[c])] and int(perm4[c])>1000:                  
                                    d1 = int(perm4[c])-int(perm4[b])
                                    if d1==d2:
                                        if (perm4[a],perm4[b],perm4[c])!=('1487','4817','8147'):
                                            return perm4[a]+perm4[b]+perm4[c]
                                else:
                                    continue
                        else:
                            continue
                else:
                    continue
        else:
            continue
        for value in perm4:
            perm_used[int(value)]=1
        
if __name__ == "__main__":
    print('The 12-digit number after concatenation of the arithmetic sequence is {0}'.format(arithmetic_sequence())) 