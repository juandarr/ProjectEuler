"""
Finds the expected number of times the foreman finds a single sheet of paper in the envelope during the week
Author: Juan Rios
"""

import math
from time import time
from utils import prime_factors

"""
Finds the expected number of times the foreman finds a single sheet of paper in the envelope during the week
"""
def expected_value():
    day = 2
    paths = [[[1,1,1,1],1]]
    prob = 0
    while day < 15:
        day+=1
        counter_unit = 0
        tmp_ar = []
        k = 0
        for path in paths:
            for idx in range(len(path[-2])):
                if path[-2][idx]>0:
                    tmp = path[-2].copy()
                    tmp[idx]-=1
                    for idx2 in range(idx+1,len(path[-2])):
                        tmp[idx2]+=1
                    if sum(tmp)==1:
                        k+=1
                    tmp_prob = path[-1]*path[-2][idx]/sum(path[-2])
                    tmp_ar.append(path[:-1]+[tmp]+[tmp_prob])
        paths =tmp_ar
    freq = {}
 
    for path in paths:
        c = 2
        k = 0
        for opt in path[:-1]:
            if sum(opt)==1:
                k+=1
            c+=1
        if k not in freq:
            freq[k]=path[-1]
        else:
            freq[k]+=path[-1]

    prob = 0
    for key in freq:
        prob += freq[key]*key
    return prob

if __name__ == "__main__":
    print('The expected value to six decimal places is {0:.6f}'.format(expected_value()))