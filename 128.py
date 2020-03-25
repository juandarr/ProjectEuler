"""
Finds the 2000th tile in the sequence of tiles being surrouded with 3 prime differences
Author: Juan Rios
"""

import math
from utils import decompose_primes,prime_factors
from time import time

def get_rings(limit_r):
    '''
    calculates all the rings from 0 to limit_r
    '''
    rings = {0:[1]}
    n = 1
    limit_p=1
    for r in range(1,limit_r+1):
        n += 6*r
        rings[r]=[i for i in range(n-6*r+1,n+1)]
        limit_p += 6*r
    return rings,limit_p

def prime_differences_tiles_brute_force(limit_r,n_th):
    rings,limit_p = get_rings(limit_r)
    print(limit_p)
    primes = prime_factors(limit_p+1, False)
    c = 0
    val = 0
    l = 0
    for tile in rings[0]:
        for tile_b in rings[1]:
            if primes[abs(tile_b-tile)]==1:
                c +=1
        if c==3:
            l +=1
            val = tile
    avoid = 0
    for i in range(1,limit_r):
        prev_ar = ([1]+[2]*(i-1))*6
        prev = prev_ar.copy()
        for idx in range(len(prev_ar)-1,-1,-1):
            prev_ar[idx]= sum(prev_ar[:idx])-idx
        next_ar = ([3]+[2]*(i-1))*6
        nex = next_ar.copy()
        for idx in range(len(next_ar)-1,-1,-1):
            next_ar[idx]= sum(next_ar[:idx])-idx-1
        for idx in range(len(rings[i])):
            if ((rings[i][idx]%2==0 and prev[idx]==2) or (rings[i][idx]%2==1 and prev[idx]==1)):
                avoid += 1
                continue
            c = 0
            voisin = []
            # Neighboor tiles from the same ring
            if primes[abs(rings[i][idx-1]-rings[i][idx])]==1:
                c += 1
            if idx+1==len(rings[i]):
                up = 0
            else:
                up = idx+1
            if primes[abs(rings[i][up]-rings[i][idx])]==1:
                c += 1
            # Neighboor tiles from previous ring
            prev_start = prev_ar[idx]
            if idx%(i)==0:
                previous_c = 1
            else:
                previous_c = 2
            for t in range(previous_c):
                if prev_start+t==len(rings[i-1]):
                    up = 0
                else:
                    up = prev_start+t
                if primes[abs(rings[i-1][up]-rings[i][idx])]==1:
                    c += 1  
            # Neighboor tiles from next ring
            next_start = next_ar[idx]
            if idx%i==0:
                next_c = 3
            else:
                next_c = 2
            for t in range(next_c):
                if primes[abs(rings[i+1][next_start+t]-rings[i][idx])]==1:
                    c += 1  
            if c==3:
                l+=1
                val =rings[i][idx]
                if l==n_th:
                    print(avoid)
                    print(l,val,prev[idx],nex[idx], primes[val])
                    return val
                else:
                    if idx==0:
                        print(l,val,prev[idx],nex[idx], i,idx)
                    else:
                        print(l,val,prev[idx],nex[idx], i,6*i-1,idx)
    print(avoid)

def is_prime(num, primes):
    '''
    returns primes that are above below_limit and below above_limit
    '''
    for p in primes:
        if p>int(math.sqrt(num)):
            return True
        elif num%p==0:
            return False

def prime_differences_tiles_alt(n_th):
    primes = prime_factors(10**6, True)
    total = 2
    r = 2
    while True:
        n = 0
        
        candidates = [6*r-1,12*r+5,6*r+1]
        c = 0
        for can in candidates:
            if is_prime(can,primes):
                c+=1
                if c==3:
                    total +=1
                    if total==n_th:
                        return 3*r**2-3*r+2+n
        n = 6*r-1
        p_prev = 2*n-(n+r-1)//r
        p_next = 2*n+(n+r-1)//r
        candidates = [6*r-1,6*r-6-p_prev+2*n,6*r-6+n,6*r-1-2*n+p_next,6*r-2*n+p_next]
        c = 0
        for can in candidates:
            if is_prime(can,primes):
                c+=1
                if c==3:
                    total +=1
                    if total==n_th:
                        return 3*(r**2)-3*r+2+n
        r += 1

if __name__ == "__main__":
    n_th = 2000
    print('The {0}th tile in the sequence of tiles being surrouded with 3 prime differences is {1}'.format(n_th,prime_differences_tiles_alt(n_th)))