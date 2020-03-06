"""
Finds the number of blue discs for arrangements of discs of over 10**12 with a probability of 50% of taking two blue discs
Author: Juan Rios
"""
import math
from itertools import combinations

def find_probability(limit_value):
    i = 0
    while True:
        f_m = 3-2*math.sqrt(2)
        f_p = 3+2*math.sqrt(2)

        t1 = (-f_m**i-math.sqrt(2)*f_m**i-f_p**i+math.sqrt(2)*f_p**i+2)/4
        b1 = (2*f_m**i+math.sqrt(2)*f_m**i+2*f_p**i-math.sqrt(2)*f_p**i+4)/8
        i += 1
        if t1>limit_value:
            return round(b1)

if __name__ == "__main__":
    limit_value = 10**12
    print('The first arrangement for blue discs of over {0} total discs with a probability of 50% of taking two blue discs is {1}'.format(limit_value, find_probability(limit_value))) 