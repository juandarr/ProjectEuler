"""
Finds the maximum prize fund that should be allocated to single random game
Author: Juan Rios
"""
import math
from itertools import combinations
from utils import decompose_primes,prime_factors

def prize_allocation(limit_n):
    '''
    returns the maximum prize fund that should be allocated to single random game of limit_n trials
    '''
    total = 1
    trials = limit_n
    for r in range(trials//2+1,trials):
        elems = [ i for i in range(trials)]
        for comb in combinations(elems,r):
            value = 1
            ar_cp = elems.copy()
            for c in comb:
                ar_cp.remove(c)
            for el in ar_cp:
                value *= (el+1)
            total += value
    den = 1
    for i in range(2,trials+2):
        den *=i
    return den//total

if __name__ == "__main__":
    limit_n = 15
    print('The maximum prize fund that should be allocated to single random game is {0}'.format(prize_allocation(limit_n)))
