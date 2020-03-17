"""
Finds the least value of n for which the variations exceeds one million
Author: Juan Rios
"""
import math

def block_counting(m):
    '''
    returns the least value of n for which the variations exceeds one million
    '''
    n = m
    variations = {}
    while True:
        counter = 1
        for block in range(m,n+1):
            for idx in range(n-block+1):
                counter +=1
                if n-(block+idx+1)>=m:
                    counter += variations[n-(block+idx+1)]
        variations[n]=counter-1
        if counter>10**6:
            return n
        n +=1
    return counter

if __name__ == "__main__":
    min_block = 50
    print('The least value of n for which the variations exceeds one million is {0}'.format(block_counting(min_block)))