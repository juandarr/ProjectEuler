"""
Finds the number of n-digit positive integers that are also an nth power
Author: Juan Rios
"""

import math

"""
Returns number of n-digit positive integers that are also an nth power
"""
def n_power_n_digits(limit_range):
    powers = [i for i in range(1,limit_range+1)]
    n_powers= {}
    for p in powers:
        number = 1
        tmp_string = str(number**p)
        while len(tmp_string)<=p:
            if len(tmp_string)==p:
                if tmp_string not in n_powers:
                    n_powers[tmp_string] = 1
                else:
                    n_powers[tmp_string] += 1
            number += 1
            tmp_string = str(number**p)
    return len(n_powers)
    
if __name__ == "__main__":
    limit_range = 21
    print('The number of n-digit positve integers thatn are also an nth power is {1}'.format(limit_range, n_power_n_digits(limit_range)))