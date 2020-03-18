"""
Finds the pandigital prime sets
Author: Juan Rios
"""
import math
from itertools import permutations,combinations
from utils import prime_factors
from time import time

def is_prime(num, primes):
    '''
    returns primes that are above below_limit and below above_limit
    '''
    for p in primes:
        if p>int(math.sqrt(num)):
            return True
        elif num%p==0:
            return False

def prime_gen(upper_limit):
    primes = [2]
    pool = {}
    pool[1]=[2]
    n = 1
    for i in range(3,upper_limit+1,2):
        is_prime = True
        for p in primes:
            if p>int(math.sqrt(i)):
                break
            if i%p==0:
                is_prime = False
                break
        if is_prime:
            if i>10**n:
                n+=1
                pool[n]=[]
            if len(str(i))==len(set(str(i))) and '0' not in str(i):
                pool[n].append(i)
            primes.append(i)
    return primes,pool

def set_variations(limit_n):
    '''
    returns possible variations of prime set for it to be palindrome
    '''
    n = 1
    variations_blocks = {}
    while n<=limit_n:
        variations_blocks[n]=[]
        for block in range(1,n+1):
            if block==n:
                variations_blocks[n].append([block])
            comb = [block]
            for idx in range(block,n-block+1):
                comb1 = comb+[idx]
                if block+idx==n:
                    variations_blocks[n].append(comb1)
                if n-(block+idx)>=1:
                    for b in variations_blocks[n-(block+idx)]:
                        if b[-1]<=comb[0]:
                            variations_blocks[n].append(b+comb1)
        n +=1
    sol = [i for i in variations_blocks[9] if len(i)>1 and sum([j for j in i if j==1])<=4]
    dict_sols =[]
    for s in sol:
        tmp = {}
        min_set = set(s)
        for i in min_set:
            tmp[i]=sum([1 for j in s if j==i])
        dict_sols.append(tmp)
    return dict_sols

def palindromic_sets(limit_n):
    t0 = time()
    primes,pool=prime_gen(10**6)
    t1 = time()
    print('Time to calculate primes: ',t1-t0)
    counter_set = 0
    # Check combinations for 1,8
    t0 = time()
    for j in pool[1]:
        for number in permutations([str(i) for i in range(1,10) if i!=j]):
            if number[-1] in ['2','4','5','6','8']:
                continue
            num = int(''.join(number))
            if is_prime(num,primes):
                counter_set+=1
    t1 = time()
    print('Time to calculate combinations of 1,8: ',t1-t0)
    t0 = time()
    #Check combinations for 1,1,7 and 2,7
    for j in combinations(pool[1],2):
        for comb in permutations([str(i) for i in range(1,10) if i not in j]):
            num = int(''.join(comb))
            if is_prime(num,primes):
                counter_set +=1

    for j in pool[2]:
        for comb in permutations([str(i) for i in range(1,10) if str(i) not in str(j)]):
            num = int(''.join(comb))
            if is_prime(num,primes):
                counter_set +=1
    t1 = time()
    print('Time to calculate combinations of 1,1,7 and 2,7: ',t1-t0)
    t0 = time()
    # Check all other combinations
    variations = set_variations(limit_n)
    for var in variations:
        if len(var)==1:
            keys=sorted(var.keys())
            for comb1 in combinations(pool[keys[0]], var[keys[0]]):
                if sorted(''.join([str(i) for i in comb1]))==sorted('123456789'):
                    counter_set +=1
        elif len(var)==2:
            if 8 in var or 7 in var:
                continue
            keys=sorted(var.keys())
            for comb1 in combinations(pool[keys[0]], var[keys[0]]):
                for comb2 in combinations(pool[keys[1]], var[keys[1]]):
                    if sorted(''.join([str(i) for i in comb1])+''.join([str(i) for i in comb2]))==sorted('123456789'):
                        counter_set +=1
        elif len(var)==3:
            if 7 in var:
                continue
            keys=sorted(var.keys())
            for comb1 in combinations(pool[keys[0]], var[keys[0]]):
                for comb2 in combinations(pool[keys[1]], var[keys[1]]):
                    for comb3 in combinations(pool[keys[2]], var[keys[2]]):
                        if sorted(''.join([str(i) for i in comb1])+''.join([str(i) for i in comb2])+''.join([str(i) for i in comb3]))==sorted('123456789'):
                            counter_set +=1
    t1 = time()
    print('Time to calculate rest of combinations: ',t1-t0)
    return counter_set

if __name__ == "__main__":
    limit_n = 9
    print('The number of sets definded by palindrom 1-9 where all elements are primes is {0}'.format(palindromic_sets(limit_n)))