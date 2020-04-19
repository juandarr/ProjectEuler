"""
Search for a maximum-sum subsequence
Author: Juan Rios
"""

import math
from time import time
from utils import prime_factors

def max_horizontal(s, maxi,rc_len):
    for i in range(rc_len):
        total = 0
        #print('Row',i)
        for j in range(rc_len*i,rc_len*(i+1)):
            total += s[j]
            if total>maxi:
                maxi= total
            if total<0:
                total =0
            #print(s[j])
    return maxi

def max_vertical(s,maxi,rc_len):
    for i in range(rc_len):
        total = 0
        #print('Col',i)
        for j in range(i,len(s),rc_len):
            total += s[j]
            if total>maxi:
                maxi= total
            if total<0:
                total =0
            #print(s[j])
    return maxi

def max_diagonal(s,maxi,rc_len):
    for j in range(0,len(s),rc_len):
        total = 0
        c = 0
        #print('Diag start',j)
        for i in range(j,-1,-rc_len):
            total+=s[i+c]
            if total>maxi:
                maxi= total
            if total<0:
                total =0
            #print(s[i+c])
            c+=1
        if j+rc_len>=len(s):
            for i_t in range(j+1,len(s)):
                total = 0
                c = 0
                #print('Diag start',i_t)
                while (i_t)+c<len(s):
                    total+=s[j-(c)*rc_len+c+(i_t-j)]
                    if total>maxi:
                        maxi= total
                    if total<0:
                        total =0
                    #print(s[j-(c)*rc_len+c+(i_t-j)])
                    c+=1
    return maxi

def max_counter_diagonal(s,maxi,rc_len):
    for j in range(rc_len-1,len(s),rc_len):
        total = 0
        c = 0
        #print('Diag start',j)
        for i in range(j,-1,-rc_len):
            total+=s[i-c]
            if total>maxi:
                maxi= total
            if total<0:
                total =0
            #print(s[i-c])
            c+=1
        if j+rc_len>=len(s):
            start = j%rc_len
            for i_t in range(start-1,-1,-1):
                total = 0
                c = 0
                #print('Diag start',i_t)
                while (i_t)-c>=0:
                    total+=s[j-c*rc_len-(c+(start-i_t))]
                    if total>maxi:
                        maxi= total
                    if total<0:
                        total =0
                    #print(s[j-c*rc_len-(c+(start-i_t))])
                    c+=1
                
    return maxi

"""
Search for a maximum-sum subsequence
"""
def maximum_subsequence(rc_len):

    s = []
    mod = 10**6
    dif = 500000
    for k in range(1,55+1):
        s.append((100003-200003*k+(300007*(k**3)))%(mod)-dif)
    for k in range(56,4*10**6+1):
        s.append((s[k-25]+s[k-56]+mod)%(mod)-dif)
    #s=[-2,5,3,2,9,-6,5,1,3,2,7,3,-1,8,-4,8]
    maxi = -float('inf')
    maxi = max_horizontal(s,maxi,rc_len)
    maxi = max_vertical(s,maxi,rc_len)
    maxi = max_diagonal(s,maxi,rc_len)
    maxi = max_counter_diagonal(s,maxi,rc_len)
    return maxi

# Wrong: 48519449

if __name__ == "__main__":
    rc_len = 2000
    print('The maximum sum-subsequence is {0}'.format(maximum_subsequence(rc_len)))