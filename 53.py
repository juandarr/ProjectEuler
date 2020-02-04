"""
Finds n choose r that exceed 1 million for values of n<= 100
Author: Juan Rios
"""

import math

"""
Returns the number of values n choose r exceeding 1 million
"""
def counter_n_choose_r(limit_value,elements):
    factorials = []
    for i in range(elements+1):
        factorials.append(math.factorial(i))
    counter = 0
    for n in range(elements,0,-1):
        for r in range(n,0,-1):
            value = factorials[n]/(factorials[n-r]*factorials[r])
            if value > limit_value:
                counter += 1
    return counter


if __name__ == "__main__":
    limit_value = 10**6
    elements = 100
    print('The number of n choose r values exceeding {0} is {1}'.format(limit_value,counter_n_choose_r(limit_value,elements))) 