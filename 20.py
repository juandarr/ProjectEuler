"""
Finds the number of digits in the number 100!
Author: Juan Rios
"""
import math

"""
Factorial function
"""

def factorial(n):
    val = 1
    for i in range(2,n+1):
        val *= i
    return val

def sum_of_digits(n):
    digits = str(n)
    total = 0
    for d in digits:
        total += int(d)
    return total 

if __name__ == "__main__":
    n = 100
    print('The sum of the digits of the number {0}! is {1}'.format(n, sum_of_digits(factorial(n))))