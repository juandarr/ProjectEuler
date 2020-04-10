"""
Finds the torricelli triangles with n+p+q<=120000
Author: Juan Rios
"""

import math
from time import time

"""
Finds the torricelli triangles with n+p+q<=120000
"""
'''
def torricelli_triangles(limit_n):
    squares ={}
    for i in range(1,10**6):
        squares[i**2]=i
    primes = prime_factors(10**6)
    counter = 0
    sti = []
    for t in range(1,100000):
        ts = t**2
        t_factors = decompose_primes(t, primes,True)
        for s in range(1,t//2+1):
            if s/t>=0.5:
                break
            valid = True
            for f in t_factors:
                if s%f==0:
                    valid = False
                    break
            if not(valid):
                break
            if (ts-3*(s**2)) in squares:
                sti.append([s,t,squares[(ts-3*(s**2))]])
                counter +=1
    print(counter)
    a = 399
    b = 455
    c = 511
    for i in sti:
        if (2*i[0]*a)%i[1]==0 and ((i[2]-i[0])*a)%i[1]==0:
            print('From a: ',(i[0],i[1]))
            print('q: {0}, r: {1}'.format(2*i[0]*a//i[1],(i[2]-i[0])*a//i[1]))
    for i in sti:
        if (2*i[0]*b)%i[1]==0 and ((i[2]-i[0])*b)%i[1]==0:
            print('From b: ',(i[0],i[1]))
            print('q: {0}, p: {1}'.format(2*i[0]*b//i[1],(i[2]-i[0])*b//i[1]))
    for i in sti:
        if (2*i[0]*b)%i[1]==0 and ((i[2]-i[0])*c)%i[1]==0:
            print('From c: ',(i[0],i[1]))
            print('p: {0}, r: {1}'.format(2*i[0]*c//i[1],(i[2]-i[0])*c//i[1]))
'''

"""
Finds the torricelli triangles with n+p+q<=120000
"""
def torricelli_triangles(limit_n):
    squares ={}
    roots = {}
    for i in range(1,10**6):
        squares[i**2]=i
        roots[i]=math.sqrt(i)
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

if __name__ == "__main__":
    limit_n = 120000
    print('The number of the torricelli triangles with n+p+q<120000 is {0}'.format(torricelli_triangles(limit_n)))