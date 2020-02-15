"""
Finds the n/d value for d<=10*6, n<d to the left of 3/7
Author: Juan Rios
"""

import math
from utils import prime_factors

'''
3/7 quot: 0.42857142857142855
One prime: 428551 999953 quot: 0.42857114284371367
One prime and 3/7: 3*142787/(7*142789) quot: 0.4285654257080627
300000/700001   quot: 0.42857081632740524
428567 999990 quot: 0.42857128571285713
428570/999997 quot: 0.42857128571385716
'''

def get_n(limit_value):
    limit_sqrt = int(math.sqrt(limit_value))
    primes = prime_factors(limit_sqrt)
    ref = 3/7
    diff = float('inf')
    num = 0
    for i in range(limit_value,0,-1):
        pivot = int(3*(i/7))
        for j in range(pivot+2,pivot-2,-1):      
            tmp = j/i
            if tmp < ref:
                if ref-tmp<diff:
                    if set(find_prime_factors(j,primes))!=set(find_prime_factors(i,primes)):
                        diff = ref-tmp
                        num = j
                break
    return num

def find_prime_factors(value,primes):
    factors = []
    for p in primes:
        if p > math.sqrt(value):
            break
        if value%p==0:
            factors+=[p,value//p]
    return factors

if __name__ == "__main__":
    limit_value = 10**6
    print('The value of n of the fraction n/d left of 3/7 is {0}'.format(get_n(limit_value)))