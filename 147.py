"""
Finds rectangles in cross-hatched grids
Author: Juan Rios
"""

import math
from time import time

def horizontal_vertical_accumulator(limit_l,limit_h):
    total = 0
    for i in range(1,limit_l+1):
        for j in range(1,limit_h+1):
            total += (limit_l-i+1)*(limit_h-j+1)
    return total

def cross_hatched(l,h,i,j):
    m = max(l,h)
    n = min(l,h)
    f = (i+j)//2
    if (i%2)+(j%2)==2:
        if n<f:
            return 0
        else:
            return (m-f)+(n-f)*(2*(m-f+1)-1)
    elif (i%2)+(j%2)==1:
        if n<=f:
            return 0
        else:
            return 2*(m-f)*(n-f)
    elif (i%2)+(j%2)==0:
        if n<f:
            return 0
        else:
            return (m-f+1)+(n-f)*(2*(m-f+1)-1)

def cross_hatched_block_generator(l,h):
    m = max(l,h)
    n = min(l,h)
    combs = []
    if m>n:
        for i in range(1,2*n):
            for c in range(1,2*n-i+1):
                combs.append((i,c))
    else:
        for i in range(1,2*n):
            if (i%2)+((2*n-i)%2)==2:
                limit = 2*n-i-1
            else:
                limit = 2*n-i
            for c in range(1,limit+1):
                combs.append((i,c))
    return combs

"""
Finds rectangles in cross-hatched grids
"""
def rectangles_cross_hatched_charts(limit_l,limit_h):
    total = 0
    for l in range(1,limit_l+1):
        for h in range(1,limit_h+1):
            total += horizontal_vertical_accumulator(l,h)
            # Now go throuhgh the cross-hatched rectangles
            for c in cross_hatched_block_generator(l,h):
                total += cross_hatched(l,h,c[0],c[1])
    '''
    for c in range(1,4):
        for j in range(1,8):
            print("\nTable for rectangles {0}x{1}".format(i,j))
            print("   1  2  3  4  5  6  7")
            for h in range(1,8):
                row = "{0}  ".format(h)
                for l in range(1,8):
                    m = max(l,h)
                    n = min(l,h)
                    val = cross_hatched(l,h,i,j)
                    row += str(val)+' '*(3-len(str(val)))
                print(row)
    '''
    return total

if __name__ == "__main__":
    limit_l = 47
    limit_h = 43
    #print(cross_hatched_block_generator(limit_l,limit_h))
    print('The amount of rectangles in cross-hatched grids is {0}'.format(rectangles_cross_hatched_charts(limit_l,limit_h)))