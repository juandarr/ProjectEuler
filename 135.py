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
def arithmetic_sequence_differences(limit_n):
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

        
if __name__ == "__main__":
    limit_n = 10**6
    print('The amound of values that solve the equation z**2-y**2-x**2=n, with 10 solutions is {1}'.format(limit_n,arithmetic_sequence_differences(limit_n)))