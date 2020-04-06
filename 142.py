"""
Finds the smallest x+y+z with several boundaries defined as perfect squares
Author: Juan Rios
"""

import math
from time import time
from decimal import *
from utils import prime_factors,divisorGen
import numpy as np

"""
Finds the smallest x+y+z with several boundaries defined as perfect squares
"""
def bounded_perfect_squares(limit_n):
    squares =[]
    squares_idx = {}
    for i in range(1, 10**5+1):
        squares_idx[i**2]=i
        squares.append(i**2)
    for k in squares:
        if k>limit_n:
            break
        mod_k = k%2
        for j in squares:
            if k<=(j+1):
                break
            m = k - j
            if m in squares_idx:
                for n in squares:
                    w = n+j
                    i = k+n
                    if k<=w:
                        break
                    if (w%2)!=mod_k:
                        continue
                    if w in squares_idx and i in squares_idx:
                        if (3*k+n-j)%2==0:
                            number = (3*k+n-j)//2
                            print(number,i,j,k,w,k-j,n)
                            return number

if __name__ == "__main__":
    limit_n = 10**8
    print('The smallest x+y+z with several boundaries defined as perfect squares is {0}'.format(bounded_perfect_squares(limit_n)))