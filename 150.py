"""
Search for a maximum-sum subsequence
Author: Juan Rios
"""

import math
from time import time
from utils import prime_factors

"""
Search for a maximum-sum subsequence
"""
def minimum_subsequence():
    t0 = time()
    t = 0
    pow2_20 = 2**20
    pow2_19 = 2**19
    limit = 1
    counter = 0
    limit = 1
    counter = 0 
    ar = [[]]
    acum = [[]]
    total = 0
    for k in range(1,500500+1):
        t = (615949*t+797807)%pow2_20
        s = t-pow2_19
        ar[-1].append(s)
        total += s
        acum[-1].append(total)
        counter +=1
        if limit==counter and k!=500500:
            total = 0
            ar.append([])
            acum.append([])
            limit+=1
            counter = 0
    minimum = float('inf')
    for row_idx in range(len(ar)):
        for idx in range(len(ar[row_idx])):
            total = ar[row_idx][idx]
            t = 1
            for row_idx2 in range(row_idx+1,len(acum)):
                total+= acum[row_idx2][idx+t]-acum[row_idx2][idx-1]
                t+=1
                if total<minimum:
                    minimum = total
    t1 = time()
    print('Time to reach solution: ', t1-t0)
    return minimum

if __name__ == "__main__":
    print('The minimum sum-subsequence is {0}'.format(minimum_subsequence()))