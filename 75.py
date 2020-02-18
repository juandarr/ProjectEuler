"""
Finds the number of values L for which the right angle triangle has only one solution
Author: Juan Rios
"""

import math
from utils import prime_factors
import time

def is_integer_solution_unique(l,squares):
    sol =[]
    upper = l//2-1-((l//2)%2)
    lower = int((math.sqrt(2)-1)*l)
    ls = l**2
    for c in range(upper, lower,-2):
        quot = 4*(l-c)**2-8*(ls-2*l*c)
        if quot in squares:
            #a = int((2*(l-c)+math.sqrt(quot))/4)
            #b = l-c-a
            #print(l,[a,b,c])
            return True
        else:
            continue
    return False

def right_angle_solutions(limit_value):
    visited = [0]*(limit_value+1) 
    squares ={}
    for i in range(int(limit_value/2)+1):
        squares[i**2]=i
    t0 = time.time()
    for l in range(2,limit_value+1):
        if visited[l]==0:
            if is_integer_solution_unique(l,squares):      
                for index in range(l, limit_value+1,l):
                    if visited[index]>0:
                        visited[index] += 1
                    else:
                        visited[index]= 1
        if l%(limit_value//2)==0:
            t1 = time.time()
            print(l, 'time to loop: {0}'.format(t1-t0))
            t0 = time.time()
    return sum([1 for i in visited if i==1])


def mcd(n,m,primes):
    tmp = n
    sqrt = math.sqrt(n)
    for p in primes:
        if p > sqrt or tmp==1:
            if tmp!=1:
                if m%tmp==0:
                    return False
            break
        if tmp%p==0:
            if m%p==0:
                return False
            tmp //= p
            while (tmp%p==0):
                tmp //= p
    return True

def phytagorean_triangle(limit_value): 
    primes = prime_factors(int(math.sqrt(limit_value))+1)
    visited = [0]*(limit_value+1)
    n = 1
    while n<limit_value:
        lower = n+1
        ns = n**2
        for m in range(lower,limit_value,2):
            if mcd(n,m,primes):
                total = sum([m**2-ns,2*m*n,m**2+ns])
                if total<=limit_value:
                    for i in range(total, limit_value+1, total):
                        visited[i] += 1
                else:
                    break
        n += 1
    return sum([1 for i in visited if i==1])

if __name__ == "__main__":
    limit_value = 1500000
    print('The number of values L for which the right angle triangle has one solution is {0}'.format(phytagorean_triangle(limit_value)))