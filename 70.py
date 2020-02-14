"""
Finds the value n< 10**7 for which n/phi(n) is a minimum and phi(n) is a permutation of n
Author: Juan Rios
"""

import math
from utils import prime_factors

def get_n_permutation(limit_value):
    primes = prime_factors(limit_value)
    min_ratio = float('inf')
    candidate = 0
    for i in range(len(primes)-1,100,-1):
        for j in range(i,100,-1):
            number = primes[i]*primes[j]
            if number < 10**7:
                phi_acum = number-1-sum([1 for c in range(primes[i],number,primes[i])])-sum([1 for c in range(primes[j],number,primes[j])])
                if sorted(str(number))==sorted(str(phi_acum)):
                    if min_ratio>(number/phi_acum):
                        min_ratio = (number/phi_acum)
                        candidate = number
    return candidate


if __name__ == "__main__":
    limit_value = int(math.sqrt(10**7))+500
    print('The number n with minimum ratio n/phi(n) and phi(n) permutation of n is {0}'.format(get_n_permutation(limit_value)))