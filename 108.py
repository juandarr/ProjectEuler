"""
Finds the least value of n for which the number of distinct solutions exceeds one thousand
Author: Juan Rios
"""
import math
from utils import prime_factors, decompose_primes, find_divisors
from itertools import combinations

def product_pairs(n):
    '''
    2. This function solves the problem finding every possible pair of factors given its prime decomposition
    '''
    primes = prime_factors(1000)
    prime_factors = decompose_primes(n,primes,as_dict=False)
    prime_factors = [1]+prime_factors
    pairs = {}
    for r1 in range(1,len(prime_factors)//2+1):
        for comb1 in combinations([i for i in range(len(prime_factors))], r1):
            a = 1
            for idx in comb1:
                a*= prime_factors[idx]
            set_a = set(decompose_primes(a,primes))
            complement = [i for i in range(len(prime_factors)) if i not in comb1]
            for r2 in range(r1,len(complement)+1):
                for comb2 in combinations(complement,r2):
                    b = 1
                    for idx in comb2:
                        b*= prime_factors[idx]
                    if set_a.isdisjoint(set(decompose_primes(b,primes))):
                        if (a,b) not in pairs and (b,a) not in pairs:
                            pairs[(a,b)]=1
    return len(pairs)+1

def solution_given_primes():
    '''
    3. This function solves the problem using the prime decomposition to calculate the number of valid solutions
    '''
    n = 180100
    primes = prime_factors(200000)
    while True:
        dec_primes = decompose_primes(n**2,primes, as_dict=True)
        divs = 1
        for p in dec_primes:
            divs *= (dec_primes[p]+1)
        if divs>1999:
            return n
            break
        n += 1
    
def find_solution(n):
    y = n+1
    x = float('inf')
    solutions = 0
    while True:
        if n*y%(y-n)==0:
            x = n*y//(y-n)
            solutions += 1
        if x==y:
            break
        y+=1
    return solutions

def explore_solutions():
    '''
    1. First solution, uses brute force to solve problem
    '''
    n=180100
    c = 1
    while True:
        sols = find_solution(n)
        if sols>50*c:
            print(n,sols)
            c += 1
        if sols>1000:
            return n
        n += 1

if __name__ == "__main__":
    print('The least value of n exceeding 1 thousand distinct solutions is {0}'.format(solution_given_primes())) 