"""
Finds the sum of all progressive numbers that also perfect squares below limit_n
Author: Juan Rios
"""

import math
from time import time
from decimal import *
from utils import prime_factors,divisorGen


"""
Finds the sum of all progressive numbers that also perfect squares below limit_n
"""
def progressive_perfect_squares(limit_n):
    total = 0
    cubes_idx ={}
    cubes =[]
    squares =[]
    fifth = []
    primes = prime_factors(10**6)
    for i in range(1, 10**6):
        cubes_idx[i**3]=i
        cubes.append(i**3)
        squares.append(i**2)
    visited = {}
    s_pow = 1*10**(int(math.log10(10**11)))
    for i in range(1,int(math.sqrt(limit_n))+1):
        n = i**2
        if n>s_pow:
            print(n,total)
            s_pow += (10**(int(math.log10(10**11))))
        for r in squares:
            if (r**2+r)>=n:
                break
            s_2 = (n-r)**2
            if s_2%r==0:
                s = s_2//r
                f = (n/r)
                if (f-1)>r and (n-r)*r in cubes_idx and s in cubes_idx:
                    print('Squared: ',n,f-1,r,(Decimal(r).sqrt(),r**(1/3)))
                    visited[n]=1
                    total += n
        if n not in visited:
            for r in cubes:
                if (r**2+r)>=n:
                    break
                s_2 = (n-r)**2
                if s_2%r==0:
                    s = s_2//r
                    f = (n/r)
                    if (f-1)>r and (n-r)*r in cubes_idx and s in cubes_idx:
                        print('Cubed: ',n,f-1,r,(Decimal(r).sqrt(),r**(1/3)))
                        visited[n]=1
                        total += n
        if n not in visited:
            divisors = divisorGen(n,primes)
            for r in divisors:
                if (r**2+r)>=n:
                    break
                s_2 = (n-r)**2
                if s_2%r==0:
                    s = s_2//r
                    f = (n/r)
                    if (f-1)>r and (n-r)*r in cubes_idx and s in cubes_idx:
                        print('Weirdo: ',n,f-1,r,(Decimal(r).sqrt(),r**(1/3)))
                        visited[n]=1
                        total += n
    return total

if __name__ == "__main__":
    limit_n = 10**12
    primes=prime_factors(10**6)
    print('The sum of all progressive numbers that also perfect squares below {0} is {1}'.format(limit_n,progressive_perfect_squares(limit_n)))