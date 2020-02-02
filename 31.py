"""
Finds all possible combinations of coins to generate value
Author: Juan Rios
"""
import math

"""
Calculate the possible combinations of coins to equate value
"""
def find_combs(coins,value, index):
    if value%coins[index]==0 and index==0:
        return 1
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
    value = 200
    coins = [1,2,5,10,20,50,100,200]
    for i in range(len(coins)-1,-1,-1):
        if (coins[i]<=value):
            index = i
            break
    print('The total possible combination to generate the value {0} is {1}'.format(value, find_combs(coins,value, index))) 