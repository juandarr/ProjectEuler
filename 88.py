"""
Finds the product-sum numbers for different set lenghs of k between 2 and 12000
Author: Juan Rios
"""
import math
from utils import prime_factors
from itertools import combinations


"""
Calculate the possible combinations of integers below n to equal n
"""
def find_combs(n):
    pass

"""
Decomposes and groups the prime factor of a number n
"""
def decompose_and_group(n,primes):
    """
    Decompose number in n prime factors and group them in groups of 2,3,...,n-1,n
    """
    prime_factors = []
    tmp = n
    for div in primes:
        if div>math.sqrt(n):
            break
        while tmp%div==0:
            tmp //= div
            prime_factors.append(div)
    if tmp>1:
        prime_factors.append(tmp)
    groups = {}
    for r in range(len(prime_factors)-1,1,-1):
        for comb in combinations(prime_factors,r):
            group = []
            tmp = list(comb)
            number_a = 1
            for i in prime_factors:
                if i in tmp:
                    number_a *=i
                    tmp.remove(i)
                else:
                    group.append(i)
            group.append(number_a)
            group.sort()
            groups[tuple(group)]=sum(group)
    groups[tuple(prime_factors)] = sum(prime_factors)
    return sorted(groups.items(), key = lambda x: x[1])

"""
Calculates the least values for each k set length
"""
def sum_product_set_length(limit_value):
    sol = {}
    k = [i for i in range(2,limit_value+1)]
    k_index = {}
    for i in k:
        k_index[i]=1
    primes = prime_factors(10000)
    primes_index = prime_factors(100000, False)
    decomposition = {}
    i = 4
    while k:
        if primes_index[i]==0:
            tmp = decompose_and_group(i,primes)
            for g in tmp:
                tmp_k = (i-g[1])+len(g[0])
                if tmp_k not in sol:
                    if tmp_k in k_index:
                        sol[tmp_k] = i
                        k.remove(tmp_k)
        i += 1
    return sum(set(sol.values()))

if __name__ == "__main__":
    limit_value = 12000
    for i in range(2,5):
        print(find_combs([s for s in range(1,i+1)],i,i-1))
    '''
    primes = prime_factors(1000)
    primes_index = prime_factors(1000,False)
    for i in range(4,100):
        if primes_index[i]==0:
            print(i,decompose_and_group(i,primes))
    '''
    #print('The sum of all minimal product-sum numbers from k>=2 to k<={0} is {1}'.format(limit_value,sum_product_set_length(limit_value)))

#wrong: 22336175
#worng: 18175719