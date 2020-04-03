"""
Finds the number of pythagorean triangles where the perimeter is less than 100 million and central small square dividing the bigger square
Author: Juan Rios
"""

import math
from time import time
from utils import decompose_primes, prime_factors
from decimal import *

"""
Finds the number of pythagorean triangles where the perimeter is less than 100 million and central small square dividing the bigger square
"""
def pythagorean_triplets(limit_n):
    primes = prime_factors(1000)
    total = 0
    t0 = time()
    for m in range(2,limit_n+1):
        if 2*m**2+2*m>=limit_n:
            break
        factors = decompose_primes(m,primes,True)
        inc = 1
        if m%2==0:
            inc = 2
        complete = False
        for n in range(1,m,inc):
            if inc==1 and n%2==1:
                continue
            are_coprime=True
            for p in factors:
                if n%p==0:
                    are_coprime = False
                    break
            if are_coprime:
                a = m**2-n**2
                b = 2*m*n
                c = m**2+n**2
                if (a+b+c)>=limit_n:
                    break
                if c%(b-a)==0:
                    print(a,b,c)
                    total += limit_n//(a+b+c)
        if complete:
            break
    t1= time()
    print('Time to reach solution: {0} sec'.format(t1-t0))
    return total

if __name__ == "__main__":
    limit_n = 10**8
    print('The number of pythagorean triangles where the perimeter is less than {0} and match condition is {1}'.format(limit_n,pythagorean_triplets(limit_n)))