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
def calculate_partitions(value,pivot):
    if value==pivot or value-pivot<pivot:
        return []
    else:
        partitions = []
        new_pivot = pivot
        while value-new_pivot>=new_pivot:
            partitions.append([value-new_pivot,new_pivot])
            new_pivot += 1
        tmp = partitions
        if tmp:
            for p in range(len(tmp)):
                tmp2 = calculate_partitions(tmp[p][0],tmp[p][1])
                for p2 in tmp2:
                    partitions += [p2+tmp[p][1:]]
    return partitions

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
    partitions = calculate_partitions(len(prime_factors),1)
    #print(partitions)
    groups = []
    c = 0
    for partition in partitions:
        if set(partition)==set([1]):
            #print(partition)
            continue
        index_p = 0
        array_partitions = [prime_factors]
        group=[]
        unity = False
        while index_p<len(partition):
            if partition[index_p]==1:
                unity = True
                break
            tmp_arrays = []
            tmp_groups = []
            if len(set(prime_factors))==1:
                tmp_arrays.append([])
                tmp_groups.append([])
                if group:
                    tmp_groups[-1] += group[idx]+[prime_factors[0]**partition[index_p]]
                else:
                    tmp_groups[-1].append(prime_factors[0]**partition[index_p])
                tmp_arrays[-1] += [prime_factors[0]]*(len(prime_factors)-sum(partition[0:index_p+1]))
            else:
                for idx in range(len(array_partitions)):
                    for comb in combinations(array_partitions[idx],partition[index_p]):
                        tmp =list(comb)
                        tmp_arrays.append([])
                        tmp_groups.append([])
                        number = 1
                        for i in array_partitions[idx]:
                            if i in tmp:
                                number *= i
                                tmp.remove(i)
                            else:
                                tmp_arrays[-1].append(i)
                        if group:
                            tmp_groups[-1] += group[idx]+[number]
                        else:
                            tmp_groups[-1].append(number)
                    #print(tmp_arrays[-1], tmp_groups[-1])
            '''
            elif len(set(prime_factors))==2 and sum([1 for i in prime_factors if i==prime_factors[0]])==(len(prime_factors)-1):
                print('do it!')
                
                for idx in range(len(array_partitions)):
                    tmp_arrays.append([])
                    tmp_groups.append([])
                    if group:
                        tmp_groups[-1] += group[idx]+[prime_factors[0]**partition[index_p]] 
                        tmp_groups.append([])
                        tmp_groups[-1] += group[idx]+[prime_factors[-1]*prime_factors[0]**(partition[index_p]-1)]
                    else:
                        tmp_groups[-1].append(prime_factors[0]**partition[index_p])
                        tmp_groups.append([])
                        tmp_groups[-1].append(prime_factors[-1]*prime_factors[0]**(partition[index_p]-1))
                    print(partition, tmp_groups)
                    tmp_arrays[-1] += [prime_factors[0]]*(len(prime_factors)-sum(partition[0:index_p+1])-1)+[prime_factors[-1]]
                    tmp_arrays.append([])
                    tmp_arrays[-1] += [prime_factors[0]]*(len(prime_factors)-sum(partition[0:index_p+1]))
            '''
            
            group = tmp_groups
            array_partitions = tmp_arrays
            #print(partition, group, array_partitions)
            index_p += 1
        if unity:
            for idx in range(len(array_partitions)):
                for i in array_partitions[idx]:
                    group[idx].append(i)
        #print(partition,group)
        groups += group
        #print(len(groups))
        #c+=1
        #if c==4:
        #    break
    gs = {}
    for group in groups:
        gs[tuple(group)]=sum(group)
    gs[tuple(prime_factors)] = sum(prime_factors)
    return sorted(gs.items(), key = lambda x: x[1])

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
        print(i)
    return sum(set(sol.values()))

if __name__ == "__main__":
    
    limit_value = 12000
    '''
    ar=[s for s in range(1,100)]
    for i in range(6,7):
        print(i,calculate_partitions(i,1))
    
    
    primes = prime_factors(1000)
    primes_index = prime_factors(1000,False)
    #30030
    for i in range(3*2**11,3*2**11+1):
        #if primes_index[i]==0:
        print(i,len(decompose_and_group(i,primes)))
    '''
    print('The sum of all minimal product-sum numbers from k>=2 to k<={0} is {1}'.format(limit_value,sum_product_set_length(limit_value)))

#wrong: 22336175
#worng: 18175719