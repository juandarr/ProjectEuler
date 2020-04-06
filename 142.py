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
    for i in range(1, 10**7+1):
        squares_idx[i**2]=i
        squares.append(i**2)
    found = False
    counter =0
    number = 0
    for idx in range(len(squares)):
        if squares[idx]>counter:
            print(squares[idx])
            counter+=10**6
            break
    for k in squares[idx:]:
        if k>limit_n:
            break
        mod_k = k%2
        if k > counter:
            print(k)
            counter+=10**6
        for j in squares:
            if j>limit_n or k<=(j+1):
                break
            if (k-j) in squares_idx and (k+j) in squares_idx:
                for n in squares:
                    nj = n+j
                    if n>limit_n or k<=nj:
                        break
                    if nj%2!=mod_k:
                        continue
                    if nj in squares_idx:
                        print('Almost there!')
                        if (3*k+n-j)%2==0:
                            print(n,j,k,nj,k-j,k+j)
                            z = (k-n-j)/2
                            print(z,z+n,z+n+j,(3*k+n-j)//2)
                            number = (3*k+n-j)//2
                            found = True
                    if found:
                        break
                if found:
                    break
        if found:
            break
    return number
'''
def solve_matrix():
    A = np.matrix([[-1,0,1,0,0,1],[0,1,-1,0,1,0],[1,0,0,-1,-1,0],[1,1,-1,-1,0,0],[0,0,1,-1,-1,1],[1,-1,0,0,-1,-1]])
    print(np.linalg.eig(A))
'''

if __name__ == "__main__":
    limit_n = 10**14
    #print(solve_matrix())
    print('The smallest x+y+z with several boundaries defined as perfect squares is {0}'.format(bounded_perfect_squares(limit_n)))