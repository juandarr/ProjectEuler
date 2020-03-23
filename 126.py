"""
Finds least value of n (n cuboids required to cover all faces of a shape) with C(n)==1000
Author: Juan Rios
"""
import math

def update_layers(dim,cub,candidates,limit_n,limit_l):
    '''
    updates C and candidates as least value of n for which C(n)==1000
    '''
    a,b,c = dim
    l = 2*(a*b+a*c+b*c)
    base = 4*(a+b+c)
    if l in cub:
        cub[l]+=1
        if cub[l]==limit_n:
            candidates.append(l)
        elif cub[l]==limit_n+1:
            candidates.remove(l)
    else:
        cub[l]=1
    mul = 0
    while l<limit_l:
        l = l + base +8*mul
        if l in cub:
            cub[l]+=1
            if cub[l]==limit_n:
                candidates.append(l)
            elif cub[l]==limit_n+1:
                candidates.remove(l)
        else:
            cub[l]=1
        mul += 1

def cuboid_explorer(limit_n,limit_l,limit_explore):
    cub = {}
    candidates = []
    for h in range(1,limit_explore):
        if 6*(h**2)>limit_l and len(candidates)>1:
            return sorted(candidates)[0]
        for w in range(h,limit_explore):
            if 2*(h*w+h*w+w*w)<limit_l:
                for d in range(w,limit_explore):
                    if 2*(h*w+h*d+w*d)<limit_l:
                        update_layers((h,w,d),cub,candidates,limit_n,limit_l)
                    else:
                        continue

if __name__ == "__main__":
    limit_n = 1000
    limit_l = 20000
    limit_explore = 10000
    print('The least value of n (n cuboids required to cover all faces of a shape) with C(n)==1000 is {0}'.format(cuboid_explorer(limit_n,limit_l,limit_explore)))