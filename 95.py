"""
Finds the smallest number of the longest amicable chain with no member above one million
Author: Juan Rios
"""
import math
from utils import prime_factors


def sum_proper_divisors(limit_value,primes):
    """
    Sum of proper divisors
    """
    sieve = [0]*(limit_value+1)
    i = 2
    while i<=limit_value:
        total = 1
        if primes[i]==0:
            sqrt_i = int(math.sqrt(i))
            if i%sqrt_i==0:
                total += sqrt_i
            for d in range(2, sqrt_i):
                if i%d==0:
                    total += d + i//d 
        sieve[i]=int(total)
        i+=1
    return sieve
    
def amicable_chain(n,limit_value,sieve,primes):
    tmp = n
    chain = [tmp]
    chain_hash = {tmp:1}
    while True:
        if tmp>limit_value or tmp==1:
            return []
        i = sieve[tmp]
        if i in chain_hash:
            chain.append(tmp)
            return chain[chain_hash[i]:]
        else:
            chain.append(tmp)
            chain_hash[tmp]=len(chain)-1
            tmp = i

def smallest_in_amicable_chain(limit_value):
    primes = prime_factors(limit_value, False)
    print('primes_calculated!')
    sieve = sum_proper_divisors(limit_value, primes)
    print('Sieve calculated')
    max_len = 0
    max_chain = []
    visited = {}
    for i in range(2,limit_value+1):
        if primes[i]==0:
            ch = amicable_chain(i,limit_value,sieve,primes)
            if len(ch)>max_len:
                max_len = len(ch)
                max_chain = ch
        if i%10**5==0:
            print (i,max_len, min(max_chain))
    return min(max_chain)

if __name__ == "__main__":
    limit_value = 10**6
    print('The smallest number of the longest amicable chain with no member above one million is {0}'.format(smallest_in_amicable_chain(limit_value))) 