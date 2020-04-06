"""
Finds the smallest x+y+z with several boundaries defined as perfect squares
Author: Juan Rios
"""

import math
from time import time

"""
Finds the smallest x+y+z with several boundaries defined as perfect squares
"""
def bounded_perfect_squares(limit_n):
    squares =[]
    squares_idx = {}
    for i in range(1, 10**5+1):
        squares_idx[i**2]=i
        squares.append(i**2)
    for idx_k in range(len(squares)):
        k = squares[idx_k]
        mod_k = k%2
        if k>limit_n:
            break
        for idx_w in range(idx_k):
            w = squares[idx_w]
            if (w%2)!=mod_k:
                continue
            if w>limit_n:
                break
            for idx_n in range(idx_w):
                n = squares[idx_n]
                if n>limit_n:
                    break
                j = w - n
                m = k - j
                i = k + n 
                if i in squares_idx and m in squares_idx and j in squares_idx:
                    if (k-w)%2==0:
                        z = 3*((k-w)//2)+w+n
                        print(z,i,j,k,w,m,n)
                        return z

if __name__ == "__main__":
    limit_n = 10**10
    print('The smallest x+y+z with several boundaries defined as perfect squares is {0}'.format(bounded_perfect_squares(limit_n)))