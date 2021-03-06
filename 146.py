"""
Finds consecutive primes pattern for values n below limit
Author: Juan Rios
"""

import math
from time import time
from utils import prime_factors

# Generator of possible values to visit
def n_generator(start, limit_n):
    i = start
    yield i
    while i<limit_n:
        i+=10
        if i%3==0 or i%7 in [0,1,2,5,6] or i%13==0:
            continue
        yield i
        

def are_consecutive_primes(num, primes):
    limit = int(math.sqrt(num+27))
    values =[1,3,7,9,13,27]
    for p in primes:
        if p>limit:
            return True
        for i in values:
            if (num+i)%p==0:
                return False

def check_others_primes(num, primes):
    limit = int(math.sqrt(num+27))
    primality = [True]*27
    values = [i for i in range(27) if i not in [0,2,6,8,12,26]]
    for p in primes:
        if p>limit:
            s = sum([1 for t in primality if t==True])
            return s
        to_remove = []
        for i in values:
            if (num+i+1)%p==0:
                to_remove.append(i)
                primality[i]=False
        for rem in to_remove:
            values.remove(rem)
        if values==[]:
            return 6
            
"""
Finds consecutive primes pattern for values n below limit
"""
def consecutive_primes(limit_n):
    primes = prime_factors(limit_n+27**2)
    print('Primes calculated!')
    total = 0
    t0 = time()
    for n in n_generator(10,limit_n):
        n2 = n**2
        if are_consecutive_primes(n2,primes):
            print('{0} is candidate!'.format(n))
            if check_others_primes(n2,primes)==6:
                print('Success!')
                total += n
            else:
                print('For ',n, ' not consecutives are generated')
    t1 = time()
    print('Total time to run through the numbers until limit_n: ',t1-t0)
    return total

if __name__ == "__main__":
    limit_n = 150*10**6
    print('The amount of consecutive primes pattern for values n below {0} is {1}'.format(limit_n,consecutive_primes(limit_n)))
