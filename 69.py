"""
Finds the value n< 10**6 for which n/phi(n) is a maximum
Author: Juan Rios
"""

import math
from utils import prime_factors

def get_n_with_maximum_ratio(limit_value):
    primes = prime_factors(100)
    div = 1
    for prime in primes:
        div *= prime
        if div>limit_value:
            return div//prime


if __name__ == "__main__":
    limit_value = 10**6
    print('The number n with maximum ratio n/phi(n) is {0}'.format(get_n_with_maximum_ratio(limit_value)))