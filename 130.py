"""
Finds the sum of the first 25 composite values for which GCD(n,10)=1 and n-1 is divisibile by A(n)
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

def repunit_divisibility(start):
    i=start
    primes = prime_factors(10**6, False)
    total = 0
    counter = 0
    while True:
        if i%2!=0 and i%5!=0 and primes[i]==0:
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
            if (i-1)%n==0:    
                total+=i
                counter +=1
        i +=1
        if counter==25:
            return total

if __name__ == "__main__":
    start = 6    
    print('The sum of the first 25 composite values for which GCD(n,10)=1 and n-1 is divisibile by A(n) is {1}'.format(start,repunit_divisibility(start)))