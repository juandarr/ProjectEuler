"""
Finds the least value of n where the repunit length exceeds 10**6
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

def repunit_divisibility(limit_n):
    i=limit_n+1
    while True:
        if i%2!=0 and i%5:
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
            if n>limit_n:    
                return i
        i +=1

if __name__ == "__main__":
    limit_n = 10**6
    print('The least value of n where the repunit length exceed {0} is {1}'.format(limit_n,repunit_divisibility(limit_n)))