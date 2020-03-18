"""
Finds the 30th number in the sequence of numbers which digit sum to some power is the number
Author: Juan Rios
"""
import math
from itertools import permutations,combinations
from time import time

def explore_powers(limit_i,limit_n):
    '''
    returns possible variations of prime set for it to be palindrome
    '''
    ar = []
    for n in range(1,limit_n+1):
        for i in range(2,limit_i+1):
            num = i**n
            if i==sum([int(j) for j in str(num)]):
                if num>10:
                    ar.append(num)
    return sorted(ar)[29] 

if __name__ == "__main__":
    limit_n = 100
    limit_i= 100
    print('The 30th number in the sequence of numbers which digit sum to some power is the number is {0}'.format(explore_powers(limit_i,limit_n)))