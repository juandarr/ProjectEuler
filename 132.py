"""
Finds the sum of the first 40 prime factors of the repunit value R(10**9)
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

"""
Finds proper divisors of n
"""
def proper_divisors(n):
    div = {}
    if n==1:
        return 0
    total = 1
    sqrt_n = math.sqrt(n)
    if n%sqrt_n==0:
        div[int(sqrt_n)]=1
    for d in range(2, int(sqrt_n)):
        if n%d==0:
            div[d]=1
            div[n//d]=1
    return sorted(div)

def repunit_divisibility_initial(limit_n):
    t0 = time()
    primes = prime_factors(10**6)
    factors_n = proper_divisors(limit_n)
    factors = []
    for i in primes:
        if i%2!=0 and i%5!=0:
            if i<=int('1'*len(str(i))):
                n = len(str(i))
                res = int('1'*n)
            else:
                n = len(str(i))+1
                res = int('1'*n)
            res = res%i
            while res!=0:
                res = 10*res+1
                res = res%i
                n +=1
            if n in factors_n:
                factors.append(i)
                if len(factors)==40:
                    t1=time()
                    print('Time to calculate solution: ',t1-t0)
                    return sum(factors)

def gcd(p,primes):
    factors_n={2:9,5:9}
    factors_p = decompose_primes(p,primes,True)
    val = 1
    for i in [2,5]:
        if i in factors_p:
            for n in range(min(factors_p[i],factors_n[i])):
                val *=i
    return val

def repunit_divisibility_improved(limit_n):
    primes = prime_factors(10**6)
    factors = []
    for i in primes[3:]:
        factor = gcd(i-1,primes)
        if (10**factor)%i==1:
            factors.append(i)
            continue
        if len(factors)==40:
            return sum(factors)
        
if __name__ == "__main__":
    limit_n = 10**9 
    print('The sum of the first 40 prime factors of the repunit value R({0}) is {1}'.format(limit_n,repunit_divisibility_improved(limit_n)))