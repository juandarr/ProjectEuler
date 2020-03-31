"""
Finds the values of n in equation z**2-y**2-x**2=n, where x,y,z are consecutive terms in an arithmetic sequence, with 10 solutions
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time


"""
Finds the solution to the equation z**2-y**2-x**2=n, where x,y,z are consecutive terms in an arithmetic sequence
"""
def arithmetic_sequence_differences_bf(limit_n):
    #primes =prime_factors(1000)
    squares = {}
    for i in range(1,10**6):
        squares[i**2]=i
    solutions = {}
    total = 0
    for n in range(1,limit_n+1):
        solutions[n]=0
        x = 1
        limit =  int(3*(n+1)/4)
        while x<=limit:
            sqr = 4*(x**2)+3*n
            #if int(-x+math.sqrt(sqr))==x:
            if sqr in squares:
                if (-x+squares[sqr])%3==0:
                    #factors =decompose_primes(x,primes,True)
                    #print(x,factors,n)
                    solutions[n]+=1
            x += 1
        #print('Final loop:  ',x-1,n, int(3*(n+1)/4))
        if solutions[n]==10:
            #factors =decompose_primes(n,primes,True)
            #print(n, factors)
            print(n)
            total += 1
    return total

def check_compatibility(u,v,k):
    z = (v-u)//4
    if (math.sqrt(4*(z**2)+k)-z)%3==0:
        return True
    return False

"""
Finds complementary products of n
"""
def divisors_arithmetic_sequence(limit_n):
    total = 0
    primes_index = prime_factors(3*10**6, False)
    t0 = time()
    for n in range(1,limit_n+1):
        subtotal = 0
        k = 3*n
        if primes_index[k]==0:
            sqrt_k = math.sqrt(k)
            for d in range(1, math.ceil(sqrt_k)):
                if k%d==0:
                    if (d%2)+((k//d)%2)!=1:
                        if check_compatibility(d,k//d,k):
                            subtotal+=1
    t1 =time()
    print('Total time to get solution: ',t1-t0)
    return total
        
if __name__ == "__main__":
    limit_n = 10**6
    solutions = 10
    print('The amount of values that solve the equation z**2-y**2-x**2=n, with {0} solutions is {1}'.format(solutions,divisors_arithmetic_sequence(limit_n)))