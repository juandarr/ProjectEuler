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
    for i in range(2,limit_n+1):
        reciprocals[i]= 1/(i*i)
    total_sum = sum([reciprocals[i] for i in reciprocals])
    print(total_sum)
    branches = [2,3,4,5,7,12,15,20,28,35]
    #branches = [2,3,4,6,7,9,10,20,28,35,36,45]
    #branches = [2,3,4,6,7,9,12,15,28,30,35,36,45]
    to_test = 0
    arr = [i for i in range(2,limit_n+1)]
    for c in branches:
        arr.remove(c)
    for r in range(2,len(branches)+1):
        for comb in combinations(branches,r):
            total = sum([reciprocals[i] for i in comb])
            # This counts the amount of values to test for sums between 2 and 80 (for the answer), and 2-45 for the initial test
            to_test+=1
            for idx1 in range(len(arr)):
                val = reciprocals[arr[idx1]]
                if val>total:
                    continue
                for idx2 in range(len(arr)-1,idx1+3,-1):
                    val2 = val + reciprocals[arr[idx2]]
                    if val2>total:
                        continue
                    for idx3 in range(idx2-1,idx1+2,-1):
                        val3 = val2 + reciprocals[arr[idx3]]
                        if val3>total:
                            continue
                        for idx4 in range(idx3-1,idx1+1,-1):
                            val4 = val3 +reciprocals[arr[idx4]]
                            if val4>total:
                                continue
                            for idx5 in range(idx4-1,idx1,-1):
                                val5 = val4+reciprocals[arr[idx5]]
                                if val5>total:
                                    continue
                                if abs(val5-total)<0.0000000001:
                                    print(comb,arr[idx1],arr[idx2],arr[idx3],arr[idx4],arr[idx5])
    print(to_test)

def combinations_test():
    arr = [1,2,3,4,5,6,7]
    for idx1 in range(len(arr)):
        for idx2 in range(len(arr)-1,idx1+3,-1):
            for idx3 in range(idx2-1,idx1+2,-1):
                for idx4 in range(idx3-1,idx1+1,-1):
                    for idx5 in range(idx4-1,idx1,-1):
                        print(arr[idx1],arr[idx2],arr[idx3],arr[idx4],arr[idx5])


if __name__ == "__main__":
    #combinations()
    limit_n = 80
    print('The possible combinations of numbers 2-85 adding whose squared reciprocals add to 1/2 is {0}'.format(squared_reciprocals(limit_n)))