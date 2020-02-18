"""
Finds the first value for which combinations of primes are over five thousand
Author: Juan Rios
"""
import math
from utils import prime_factors

"""
Calculate the possible combinations of primes
"""
def find_combs(coins,value, index):
    if value%coins[index]==0 and index==0:
        return 1
    if index==0:
        return 0
    else:
        max_counter = value//coins[index]
        combs = 0
        if value%coins[index]==0:
            combs += 1
            max_counter -= 1
        for i in range(max_counter, -1, -1):
            tmp_value = value - i*coins[index]
            combs += find_combs(coins, tmp_value, index-1)
        return combs

def combinations_over_value(limit_value):
    primes = prime_factors(100)
    primes_index = prime_factors(100, False)
    value = 3
    index = 0
    solution = find_combs(primes,value,index)
    while solution <= limit_value:
        if primes_index[value]==1:
            index +=1
        value += 1
        solution = find_combs(primes,value,index)
    return value
        
if __name__ == "__main__":
    limit_value = 5000
    print('The first number with generated by over {0} combinations of primes below that number is {1}'.format(limit_value, combinations_over_value(limit_value))) 