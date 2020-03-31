"""
Finds the values of n in equation z**2-y**2-x**2=n, where x,y,z are consecutive terms in an arithmetic sequence, with 1 solutions
Author: Juan Rios
"""

import math
from utils import prime_factors
from time import time
from functools import reduce

"""
Decomposes n in prime factors 
"""
def decompose_primes(n,primes):
    """
    Decompose number in n prime factors and group them in groups of 2,3,...,n-1,n
    """
    prime_factors = []
    tmp = n
    for div in primes:
        counter= 0
        if div>math.sqrt(n):
            break
        while tmp%div==0:
            tmp //= div
            counter +=1
        if counter>0:
            yield (div,counter)        
            #prime_factors.append((div,counter))
    if tmp>1:
        prime_factors.append((tmp,1))
        yield (tmp,1)
    #return prime_factors
    return

def divisorGen(n,primes):
    factors = list(decompose_primes(n,primes))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def check_compatibility(u,v,k):
    z = (v-u)//4
    if (math.sqrt(4*(z**2)+k)-z)%3==0:
        return True
    return False

"""
Finds complementary products of n
"""
def divisors_arithmetic_sequence(limit_n,solutions):
    total = 0
    primes_index = prime_factors(3*limit_n, False)
    print('Primes calculated!')
    #primes = prime_factors(10**4)
    t0 = time()
    p = 1
    for n in range(1,limit_n+1):
        if n > p*10**6:
            print('Now in: ',p)
            p += 1
        subtotal = 0
        k = 3*n
        if primes_index[k]==0:
            if n%4 in (0,3):
                sqrt_k = math.sqrt(k)
                #factors = divisorGen(k,primes)
                #factors = decompose_primes(n,primes)
                for d in range(1, math.ceil(sqrt_k)):
                    if k%d==0:
                        if (d%2)+((k//d)%2)!=1:
                            if check_compatibility(d,k//d,k):
                                subtotal+=1
                                if subtotal>solutions:
                                    break
        if subtotal==solutions:
            #print(k,list(factors))
            total += 1
    t1 =time()
    print('Total time to get solution: ',t1-t0)
    return total
        
if __name__ == "__main__":
    limit_n = 50*10**6
    solutions = 1
    print('The amount of values that solve the equation z**2-y**2-x**2=n, with {0} solutions is {1}'.format(solutions,divisors_arithmetic_sequence(limit_n,solutions)))