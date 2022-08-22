"""
Finds the smallest number that can be divided by the numbers from 1 to n
Author: Juan Rios
"""
import math
import itertools

# Finds the largest palindrome producto of two 3 digit factors
def smallest_number(n):
    factors = {}
    for number in range(2,n+1):
        temp =  number
        isPrime= True
        for i in itertools.chain([2],range(3,math.floor(math.sqrt(number))+1,2)):
            factor = 0
            while(temp%i==0):
                factor += 1
                isPrime = False
                if i in factors.keys():
                    if factor>factors[i]:
                        factors[i] += 1
                else:
                    factors[i] = 1
                temp /= i
            if temp==1:
                break
        if isPrime:
            factors[number] = 1
    total = 1
    for key in factors:
        total *= pow(key,factors[key])
    return total

if __name__ == "__main__":
    n = 20
    print('The smallest number that can be divided by numbers from 1 to {0} is {1}'.format(n,smallest_number(n)))
