"""
Finds the possible combinations of numbers 2-85 adding whose squared reciprocals add to 1/2
Author: Juan Rios
"""

import math
from math import factorial
from time import time
from utils import prime_factors
from itertools import combinations
"""
Finds the possible combinations of numbers 2-85 adding whose squared reciprocals add to 1/2
"""
def squared_reciprocals(limit_n):
    reciprocals = {}
    for i in range(2,81):
        reciprocals[i]= 1/(i*i)
    total_sum = sum([reciprocals[i] for i in reciprocals])
    print(total_sum)
    branches = [2,3,4,5,7,12,15,20,28,35]
    #branches = [2,3,4,6,7,9,10,20,28,35,36,45]
    #branches = [2,3,4,6,7,9,12,15,28,30,35,36,45]
    for r in range(1,len(branches)+1):
        for comb in combinations(branches,r):
            total = sum([reciprocals[i] for i in comb])



if __name__ == "__main__":
    limit_n = 80
    print('The possible combinations of numbers 2-85 adding whose squared reciprocals add to 1/2 is {0}'.format(squared_reciprocals(limit_n)))