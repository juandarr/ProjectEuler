"""
Finds the amount of reversible numbers below limit_n
Author: Juan Rios
"""

import math
from time import time

# Iterator to create values to run in the algorithm
class Range_reverse:
    def __init__(self, start,limit_n):
        self.current_value = start
        self.limit = 10**7
        self.maximum = limit_n
 
    def __iter__(self):
        return self
 
    def __next__(self):
        self.current_value += 2
        if self.current_value > self.maximum:
            raise StopIteration
        if self.current_value > self.limit:
            self.current_value = self.limit+10**7+1
            self.limit += 2*10**7
        return self.current_value

# Generator of possible values to visit
def reverse_generator(start, limit_n):
    i = start
    max_gap = 10**7
    while i<limit_n:
        i+=2
        if i>max_gap:
            i=max_gap+10**7+1
            max_gap += 2*10**7
        yield i
"""
Finds the amount of reversible numbers below limit_n
"""
def reversible_numbers(limit_n):
    total = 0
    start = 13
    power = 10**7
    t0 = time()
    for n in reverse_generator(start,limit_n):
        n_str = str(n)
        if int(n_str[0])%2==0:
            carry = 0
            valid = True
            for i in range(len(n_str)):
                val = int(n_str[i])+int(n_str[-1-i])+carry
                carry = 0
                if val>=10:
                    carry = 1
                    val %= 10
                if val%2==0:
                    valid = False
                    break
            if valid:
                total += 2
        if n > power:
            print(n)
            power += 2*10**7
    t1 = time()
    print('Total time to reach the solution: ', t1-t0)
    return total

if __name__ == "__main__":
    limit_n = 10**8
    print('The amount of reversible numbers below limit_n is {0}'.format(reversible_numbers(limit_n)))