"""
Finds the number of continued fractions sqrt(N) for N=e**2 and calculates the 100th convergent
Author: Juan Rios
"""

import math
from utils import prime_factors

def get_sequence_period_e(term):
    sequence = [2]
    tmp = [1,1,2]
    while len(sequence)<term:
        tmp[2] += 2
        sequence += tmp
    return sequence

def sum_digits_100th(term):
    sequence = get_sequence_period_e(term)
    a = 2
    b = 3
    for i in sequence[:term-2]:
        tmp = b
        b = b*i+a
        a = tmp
    return sum([int(i) for i in str(b)])

if __name__ == "__main__":
    term = 100
    print('The {0}th convergent of the continued fractions for e is {1}'.format(term,sum_digits_100th(term)))