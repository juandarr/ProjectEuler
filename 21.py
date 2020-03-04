"""
Finds the sum of all  numbers below 10000
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
    for d in range(2, int(sqrt_n)):
        if n%d==0:
            total += d + n//d 
    return total

def amicable_sum(n):
    amicable_total = 0
    is_amicable = [0]*(n)
    for i in range(2, n):
        j = sum_proper_divisors(i)
        if i!=j:
            if i==sum_proper_divisors(j):
                if is_amicable[i]==0:
                    amicable_total += i
                    is_amicable[i]=1
                if j < n and is_amicable[j]==0:
                    amicable_total += j
                    is_amicable[j]=1
    return amicable_total

if __name__ == "__main__":
    limit_n = 10000
    print('The sum of all amicable numbers below {0} is {1}'.format(limit_n, amicable_sum(limit_n)))