"""
Finds the expected number of times the foreman finds a single sheet of paper in the envelope during the week
Author: Juan Rios
"""

import math
from time import time
from utils import prime_factors

def calculate_expected_value(options):
    for group in options[0]:
        for group2 in options[1]:
            for group3 in options[2]:
                for group4 in options[3]:
                    print(group,group2,group3,group4)

"""
Finds the expected number of times the foreman finds a single sheet of paper in the envelope during the week
"""
def expected_value():
    day = 2
    options = [[[[[1,1,1,1]]]]]
    total = 1
    sheet_unit=0
    prob = 0
    while day < 15:
        day+=1
        counter_unit = 0
        level = []
        for lev in options[-1]:
            for group in lev:
                tmp_group=[]
                for opt in group:
                    tmp_ar = []  
                    for idx in range(len(opt)):
                        if opt[idx]>0:
                            tmp = opt.copy()
                            tmp[idx]-=1
                            for idx2 in range(idx+1,len(opt)):
                                tmp[idx2]+=1
                            tmp_ar.append(tmp)
                    tmp_group.append(tmp_ar)
                level.append(tmp_group)
        options.append(level)
    c = 2
    for level in options:
        ones = 0
        counter=0
        
        for group in level:
            for opt in group:
                for i in opt:
                    if sum(i)==1:
                        ones +=1
                    counter+=1
        prob += ones/counter
        print(c,ones,counter)
        c+=1
    sol =calculate_expected_value(options)

    return prob

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

if __name__ == "__main__":
    print('The expected value to six decimal places is {0:.6f}'.format(expected_value()))