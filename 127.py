"""
Finds the sum of all abc-hits for c<120000
Author: Juan Rios
"""
import math
from utils import decompose_primes,prime_factors
from time import time

def multiply(ar):
    p = 1
    for i in ar:
        p*=i
    return p

def radicals(limit_n):
    '''
    finds radicals for every prime number below limit_n
    '''
    radicals = {}
    primes = prime_factors(limit_n)
    for i in range(1,limit_n):
        radicals[i]=list(decompose_primes(i,primes,True).keys())
    square_free = [0]*(limit_n+1)
    for p in primes:
        for i in range(p*p,limit_n,p*p):
            square_free[i]=1
    return radicals,square_free

def find_abc_hits(limit_n):
    counter = 0
    total = 0
    t0 = time()
    radical,square_free = radicals(limit_n)
    for c in range(limit_n-1,0,-1):
        if square_free[c]==1:
            rad_c = c/multiply(radical[c])
            for b in range(c-1, 0,-1):
                if square_free[b]==1:
                    a = c - b
                    if a < b:
                        tmp = radical[b]+radical[c]
                        l = len(tmp)
                        tmp = set(tmp)
                        if len(tmp)==l:
                            prod = multiply(radical[a])*multiply(radical[b])
                            if prod<rad_c:
                                counter +=1
                                total += c
                                print(a,b,c)
                    else:
                        break
    t1 = time()
    print('Total time for solution: ',t1-t0)
    return counter,total

if __name__ == "__main__":
    limit_n = 120000
    print('The sum of all abc-hits for c<120000 is {0}'.format(find_abc_hits(limit_n)))