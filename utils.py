import math
from functools import reduce
from sympy.ntheory import factorint
from functools import reduce

def is_prime(num, primes):
    '''
    returns primes that are above below_limit and below above_limit
    '''
    limit = int(math.sqrt(num))
    for p in primes:
        if p>limit:
            return True
        elif num%p==0:
            return False
            
"""
 Returns an array with prime numbers using the prime sieve
 This array can be in two forms:
    - An array of the primes themselves
    - Array of ones and zeros, where value is one where the index corresponds to a prime number
"""
def prime_factors(upper_limit, explicit_primes = True):
    values = [1]*(upper_limit+1)
    values[0] = 0
    values[1] = 0
    for i in range(4,upper_limit+1,2):
        values[i] = 0
    current_value = 3
    while (current_value<upper_limit):
        if values[current_value]==1:
            for i in range(2*current_value,upper_limit+1,current_value):
                values[i] = 0
        current_value += 2
    if not(explicit_primes):
        return values
    else:
        primes = []
        for i in range(len(values)):
            if values[i]==1:
                primes.append(i)
        return primes

"""
Calculate the combinations of n elements in k places
"""
def elements_comb_k(elements,k):
    comb = []
    n = len(elements)
    for i in elements:
        comb.append(i)
    while (k>1):
        tmp = []
        for i in comb:
            for j in elements:
                if str(j) not in i:
                    if set(i+str(j)) not in tmp:
                        tmp.append(set(i+str(j)))
        k -= 1
        comb = []
        for elem in tmp:
            comb.append(''.join(sorted(elem)))
    return comb
    

"""
Calculate permutations of n elements in k positions
"""
def elements_perm_k(elements,k):
    perm = []
    n = len(elements)
    for i in elements:
        perm.append(i)
    while (k>1):
        tmp = []
        for i in perm:
            for j in elements:
                if str(j) not in i:
                    tmp.append(i+str(j))
        k -= 1
        perm = tmp
    return perm

def find_divisors(n):
    """
    Find divisors of n
    """
    #div = []
    count = 0
    sqrt_n = int(math.sqrt(n))
    if sqrt_n**2==n:
        count += 1
        #div.append(sqrt_n)
    for d in range(1, sqrt_n):
        if n%d==0:
            #div.append(d)
            #div.append(n//d)
            count += 2 
    return count

'''
This function calculates the divisors of n given its prime decomposition
'''
def divisorGen(n,primes):
    #t0 = time()
    #factors = decompose_primes(n,primes)
    factors = factorint(n)
    factors =[(key,factors[key]) for key in factors]
    #t1 = time()
    #print('Time to get primes: ',t1-t0)
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                #t2 = time()
                #print('Time to use generator: ',t2-t1)
                return

"""
Decomposes n in prime factors 
"""
def decompose_primes(n,primes,as_dict=False):
    """
    Decompose number in n prime factors and group them in groups of 2,3,...,n-1,n
    """
    if as_dict:
        prime_factors = {}
    else:
        prime_factors = []
    tmp = n
    for div in primes:
        if div>math.sqrt(n):
            break
        while tmp%div==0:
            tmp //= div
            if as_dict:
                if div in prime_factors:
                    prime_factors[div]+=1
                else:
                    prime_factors[div]=1
            else:
                prime_factors.append(div)
    if tmp>1:
        if as_dict:
            if tmp in prime_factors:
                prime_factors[tmp]+=1
            else:
                prime_factors[tmp]=1
        else:
            prime_factors.append(tmp)
    return prime_factors