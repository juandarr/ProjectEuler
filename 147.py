"""
Finds rectangles in cross-hatched grids
Author: Juan Rios
"""

import math
from time import time
from utils import prime_factors

# Generator of possible values to visit
def n_generator(start, limit_n):
    i = start
    yield i
    while i<limit_n:
        i+=10
        if i%3==0 or i%7 in [0,1,2,5,6] or i%13==0:
            continue
        yield i

def horizontal_vertical(limit_l,limit_h):
    total = 0
    for i in range(1,limit_l+1):
        for j in range(i,limit_h+1):
            if i==j:
                total += (limit_l-i+1)**2
                #print(i,j,(limit_l-i+1)**2,(limit_l,limit_h))
            else:
                total += 2*(limit_l-i+1)*(limit_h-j+1)
                #print(i,j,2*(limit_l-i+1)*(limit_h-j+1),(limit_l,limit_h))
    return total

"""
Finds rectangles in cross-hatched grids
"""
def rectangles_cross_hatched(limit_l,limit_h):
    total = horizontal_vertical(limit_l,limit_h)
    # Now go throuhgh the cross-hatched rectangles
    for i in range(1,3):
        for j in range(1,8):
            print("\nTable for rectangles {0}x{1}".format(i,j))
            print("   1  2  3  4  5  6  7")
            for h in range(1,8):
                row = "{0}  ".format(h)
                for l in range(1,8):
                    m = max(l,h)
                    n = min(l,h)
                    inc = (max(i,j)+1)//2
                    if i%2+j%2==2:
                        if n<inc:
                            row += '0  '
                        else:
                            val = (m-inc)+(n-inc)*(2*(m-inc+1)-1)
                            row += str(val)+' '*(3-len(str(val)))
                    elif (i%2+j%2)==1:
                        if n<=inc:
                            row += '0  '
                        else:
                            val = 2*(m-inc)*(n-inc)
                            row += str(val)+' '*(3-len(str(val)))
                    elif i%2+j%2==0:
                        f = max(i,j)//2
                        if n<=inc:
                            row += '0  '
                        else:
                            val = (m-f)+(n-f-1)*(2*(m-f)-1)
                            row += str(val)+' '*(3-len(str(val)))
                print(row)
    '''
    for i in range(1,5):
        for j in range(i,5):
            print("\nTable for rectangles {0}x{1}".format(i,j))
            print("   1  2  3  4  5  6  7")
            for h in range(1,8):
                row = "{0}  ".format(h)
                for l in range(1,8):
                    m = max(l,h)
                    n = min(l,h)
                    inc = (j+1)//2
                    f =  i
                    if i%2==0:
                        f -= 1
                    if n<i:
                        row += '0  '
                    else:
                        val = (m-f)+(n-j)*(2*(m-i+1)-1)
                        row += str(val)+' '*(3-len(str(val)))
                print(row)
            break
    '''






if __name__ == "__main__":
    limit_l = 4
    limit_h = 4
    print('The amount of rectangles in cross-hatched grids is {0}'.format(rectangles_cross_hatched(limit_l,limit_h)))