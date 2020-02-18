"""
Finds all possible combinations of integers below value to generate value
Author: Juan Rios
"""
import math

"""
Calculate the possible combinations of integers from 1 to 99 to sum 100
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

if __name__ == "__main__":
    value = 100
    coins = [i for i in range(1,value)]
    print('The total possible combination of integers to generate the value {0} is {1}'.format(value, find_combs(coins,value,len(coins)-1))) 