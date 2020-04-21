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
    paths = [[[1,1,1,1]]]
    while day < 15:
        day+=1
        counter_unit = 0
        tmp_ar = []
        for path in paths:
            for idx in range(len(path[-1])):
                if path[-1][idx]>0:
                    tmp = path[-1].copy()
                    tmp[idx]-=1
                    for idx2 in range(idx+1,len(path[-1])):
                        tmp[idx2]+=1
                    tmp_ar.append(path+[tmp])
        paths =tmp_ar
    freq = {}
    for path in paths:
        k = 0
        for opt in path:
            if sum(opt)==1:
                k+=1
        if k not in freq:
            freq[k]=1
        else:
            freq[k]+=1
    print(len(paths),freq)
    sol  = 0
    for key in freq:
        sol += key*freq[key]
    return sol/len(paths)

# Wrong: 0.264940
# Wrong: 0.108130
# Wrong: 0.108129
# Wrong: 0.120264
# Wrong: 0.120265
# Wrong: 0.353341
# Wrong: 0.088401
# Wrong: 8.840072
# Wrong: 12.026393
# Wrong: 1.683695
# Wrong: 1.237610
# Wrong: 1.414411
# Wrong: 0.150116
# Wrong: 2.101627
# Wrong: 0.450349
# Wrong: 0.386195
# Wrong: 1.158585
# Wrong: 5.406731
# Wrong: 0.333666
# Wrong: 0.385514
# Wrong: 0.385515

if __name__ == "__main__":
    print('The expected value to six decimal places is {0}'.format(expected_value()))