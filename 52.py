"""
Finds smallest positive integer x where 2x, 3x, 4x, 5x, 6x have the same digits
Author: Juan Rios
"""

import math
from utils import elements_perm_k

"""
Returns smallest positive integer x where 2x, 3x, 4x, 5x, 6x have the same digits
"""
def permuted_multiples(permutations):
    for p in range(6, permutations+1):
        perm = elements_perm_k('123456789',p)
        for number in perm:
            if int(number[0])>1 or int(number[1])>6 or number[1:3] in ['67','68','69']:
                break
            number_int = int(number)
            number_set = set(number)
            valid = True
            for mul in range(2,7):
                if set(str(mul*number_int))!=number_set:
                    valid = False
                    break
            if valid:
                return number


if __name__ == "__main__":
    permutations = 9
    print('The smallest positive integer x where 2x, 3x, 4x, 5x, 6x have the same digits is {0}'.format(permuted_multiples(permutations))) 