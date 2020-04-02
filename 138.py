"""
Finds the sum of L, the side of an isosceles triangles with h = b+-1 and b,L, positive integers
Author: Juan Rios
"""

import math
from time import time
from utils import decompose_primes, prime_factors
from decimal import *

"""
Finds the sum of L, the side of an isosceles triangles with h = b+-1 and b,L, positive integers
"""
def isosceles_nuggets(n_th):
    r = Decimal(5).sqrt()
    a = 9-4*r
    b = 9+4*r
    sols = []
    for n in range(n_th):
        s1 = 2*(a**n)+r*(a**n)+2*(b**n)-r*(b**n)
        s2 = -2*(a**n)-r*(a**n)-2*(b**n)+r*(b**n)
        l = 5*(a**n)+2*r*(a**n)+5*(b**n)-2*r*(b**n)
        for s in [s1,s2]:
            if s > 5:
                s_rounded = round(s)
                if (s_rounded-1)%5==0:
                    val1 = (s_rounded-1)//5
                    if (val1+1)%2==0:
                        sols.append(round(l))  
                if (s_rounded+1)%5==0:
                    val2 = (s_rounded+1)//5
                    if (val2-1)%2==0:
                        sols.append(round(l))
    sols= sorted(sols)
    return sum(sols[:12])

if __name__ == "__main__":
    n_th = 200
    print('The the sum of L, the side of an isosceles triangles with h = b+-1 and b,L, positive integers is {0}'.format(isosceles_nuggets(n_th)))