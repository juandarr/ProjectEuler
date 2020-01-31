"""
Finds the next triangle number after T285=P165=H143 that is also pentagonal and hexagonal
Author: Juan Rios
"""

import math

"""
Return next number that is hexagonal, pentagonal and triangle
"""
def geometric_number(starting_index):
    c = starting_index
    while True:
        num = c*(2*c-1)
        # Checking triangle number is not necessary since every hexagonal number is also a triangle number
        b = (1+math.sqrt(1+24*num))/6
        if b == int(b):
            return num
        c += 1

if __name__ == "__main__":
    print('The next number after T285 that is pentagonal and hexagonal is {0}'.format(geometric_number(144))) 