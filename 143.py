"""
Finds the torricelli triangles with n+p+q<=120000
Author: Juan Rios
"""

import math
from time import time

"""
Finds the torricelli triangles with n+p+q<=120000
"""
def torricelli_triangles(limit_n):
    squares ={}
    for i in range(1,10**6):
        squares[i**2]=i
    sum_pqr = 0
    visited = {}
    t0 = time()
    for p in range(1,limit_n):
        if 2*p>limit_n: break
        for q in range(p,limit_n):
            if p+2*q>limit_n: break
            b2 = p**2+p*q+q**2
            if b2 in squares:
                for r in range(q,limit_n):
                    if p+q+r>limit_n: break
                    a2 = r**2+r*q+q**2
                    c2 = r**2+r*p+p**2
                    if a2 in squares and c2 in squares:
                        print((squares[a2],squares[b2],squares[c2]),(p,q,r),p+q+r)
                        total = p+q+r
                        if total not in visited:
                            sum_pqr += total
                            visited[total]=1
                        else:
                            print('Already visited!',total)
    t1 = time()
    print('Total time to calculate solution: ', t1-t0)
    return sum_pqr

# It took about one hour to reach the solution. Look at it later for a better algorithm.
if __name__ == "__main__":
    limit_n = 120000
    print('The number of the torricelli triangles with n+p+q<120000 is {0}'.format(torricelli_triangles(limit_n)))