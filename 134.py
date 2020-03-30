"""
Finds the sum S for every consecutive pair of primes (p1,p2) for p>=5 and p <=10**6
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

"""
Finds primes pair connections and adds them
"""
def prime_pair_connection_initial(limit_n):
    primes = prime_factors(10**6+200)
    n = 1
    pow_n=10
    total = 0
    t0 = time()
    for idx in range(2,len(primes)-1):
        if primes[idx]>limit_n:
            return total
        i = 1
        if primes[idx]>10**n:
            n+=1
            pow_n = 10**n
        while True:
            if (i*pow_n+primes[idx])%primes[idx+1]==0:
                val = i*pow_n+primes[idx]
                total += val
                #print(i,primes[idx], primes[idx+1],val)
                break
            i += 1
        if idx%10000==0:
            t1 = time()
            print(idx, '--> Time to complete this iteration: ', t1-t0)
            t0 = time()

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

"""
Finds primes pair connections and adds them
"""
def prime_pair_connection(limit_n):
    primes = prime_factors(10**6+200)
    pow_n=10
    total = 0
    t0 = time()
    for idx in range(2,len(primes)-1):
        if primes[idx]>limit_n:
            return total
        d = primes[idx+1]-primes[idx]
        if primes[idx]>pow_n:
            pow_n *= 10
        total += pow_n*((modinv(pow_n,primes[idx+1])*d)%(primes[idx+1]))+primes[idx]
        if idx%10000==0:
            t1 = time()
            print(idx, '--> Time to complete this iteration: ', t1-t0)
            t0 = time()
    return total
        
if __name__ == "__main__":
    limit_n = 10**6
    print('The sum S for every consecutive pair of primes (p1,p2) for p>=5 and p <={0} is {1}'.format(limit_n,prime_pair_connection(limit_n)))