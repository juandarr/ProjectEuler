import math

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
def elements_comb_k(elements,k, as_index = False):
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