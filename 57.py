"""
Finds the fractions with more digits in numerators than denominators for sqrt(2)
Author: Juan Rios
"""

import math
from utils import prime_factors

"""
Returns the number of fractions with more digits in numerator than denominator
"""
def more_digits_in_numerator():
    tmp_num = 1
    den = 2
    counter = 0
    for i in range(1000):
        num = tmp_num + den
        if len(str(num))> len(str(den)):
            counter += 1
        tmp = tmp_num
        tmp_num = den
        den = 2*den + tmp
    return counter

if __name__ == "__main__":
    print('The number of fractions with more digits in the numerator than in the denominator is {0}'.format(more_digits_in_numerator()))