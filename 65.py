"""
Finds the number of continued fractions sqrt(N) for N=e**2 and calculates the 100th convergent
Author: Juan Rios
"""

import math
from utils import prime_factors

def get_sequence_period_e():
    sequence = [2,1,2]
    tmp = [1,1,2]
    while len(sequence)<107:
        tmp[2] += 2
        sequence += tmp
    return sequence

def sum_digits_100th():
    sequence = get_sequence_period_e()[2:]
    a = 2
    b = 3
    for i in range(len(sequence[:100-2])):
        tmp = b
        b = b*sequence[i]+a
        a = tmp
    return sum([int(i) for i in str(b)])

if __name__ == "__main__":
    print('The 100th convergent of the continued fractions for e is {0}'.format(sum_digits_100th()))