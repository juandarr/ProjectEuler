"""
Finds in how many ways a row of n block can be filled with colored blocks of 2,3 and 4
Author: Juan Rios
"""
import math

def coloured_block_counting(limit_n):
    '''
    returns the number of ways a row of n block can be filled with colored blocks of 2,3 and 4
    '''
    n = 1
    variations=[{1:0},{1:0},{1:0}]
    while n<=limit_n:
        for block in [2,3,4]:
            counter = 0
            for idx in range(n-block+1):
                counter +=1
                if n-(block+idx)>=block:
                    counter += variations[block-2][n-(block+idx)]
            variations[block-2][n]=counter
        n += 1
    return sum([variations[i][limit_n] for i in range(3)])

if __name__ == "__main__":
    limit_n = 50
    print('The number of ways a row of n block can be filled with colored blocks of 2,3 and 4 is {0}'.format(coloured_block_counting(limit_n)))