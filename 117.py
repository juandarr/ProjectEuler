"""
Finds in how many ways a row of n block can be filled with colored blocks of 2,3 and 4
Author: Juan Rios
"""
import math

def colored_block_counting(limit_n):
    '''
    returns the number of ways to fill a n block row
    '''
    n = 1
    variations = {}
    while n<=limit_n:
        counter = 1
        for block in range(2,5):
            for idx in range(n-block+1):
                counter +=1
                if n-(block+idx)>=2:
                    counter += variations[n-(block+idx)]
        variations[n]=counter-1
        n +=1
    return counter

if __name__ == "__main__":
    limit_n = 50
    print('The ways a row of {0} block can be filled with red blocks of 3 of more and spacing of 1 is {1}'.format(limit_n,colored_block_counting(limit_n)))