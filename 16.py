"""
Finds the sum of the digits of 2*1000
Author: Juan Rios
"""
import math

"""
This functions generates the solution using triangle numbers
"""
def digits_sum(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total
    
if __name__ == "__main__":
    n = 2**1000
    print('The sum of the digits of the number {0} is {1}'.format(n,digits_sum(n)))
