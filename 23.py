"""
Finds the sum of all numbers that can be expressed as the sum of two abundant numbers
Author: Juan Rios
"""
import math

"""
Sum of proper divisors
"""
def sum_proper_divisors(n):
    if n==1:
        return 0
    total = 1
    sqrt_n = math.sqrt(n)
    if n%sqrt_n==0:
        total += sqrt_n
        limit_range = int(sqrt_n)
    else:
        limit_range = int(sqrt_n) + 1
    for d in range(2, limit_range):
        if n%d==0:
            total += d + n//d 
    return total

def abundant(n):
    abundant = []
    for i in range(2,n+1):
        if i < sum_proper_divisors(i):
            abundant.append(i)
    sum_abundant = [0]*(n+1)
    for index in range(len(abundant)):
        value = abundant[index]
        for addition in range(index, len(abundant)):
            if (value+abundant[addition])<(n+1):
                sum_abundant[value+abundant[addition]] = 1
    total = 0
    for i in range(1,n+1):
        if sum_abundant[i]==0:
            total += i
    return total

if __name__ == "__main__":
    limit_n = 28123
    print('The sum of all numbers that can be expressed as the sum of two abundant numbers is {1}'.format(limit_n, abundant(limit_n)))