"""
Finds the number of partition for integers from 1 to n-1, to add to n
Author: Juan Rios
"""
import math
import numpy as np

"""
Calculate the possible number of partitions
"""
def pentagonal_number_theorem(limit_value):
    pentagonal = []
    for k in range(1,10000):
        pentagonal.append((k*(3*k-1))//2)
        pentagonal.append((-k*(-3*k-1))//2)
    p={0:1,1:1}
    n = 2
    while True:
        total = 0
        index = 0
        while n>=pentagonal[index]:
            val = (index+2)//2
            if index%2==0:
                total += (-1)**(val-1)*p[n-pentagonal[index]]
            else:
                total += (-1)**(val+1)*p[n-pentagonal[index]]
            index += 1
        p[n] = total
        if total%10**6==0:
            return n
        n += 1

if __name__ == "__main__":
    limit_value = 40000
    print('The least value of n for which p(n) is divisible by one million is {0}'.format(pentagonal_number_theorem(limit_value))) 