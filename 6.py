"""
Finds the difference between the sum of the squares and the square of the sum 
Author: Juan Rios
"""
import math


# Finds the difference between the sum of the squares and the square of the sum 
def difference(n):
    sum_squares = 0
    square_sum = 0
    for i in range(1,n+1):
        sum_squares += i**2
        square_sum += i
    return (square_sum**2 - sum_squares)

if __name__ == "__main__":
    value = 100
    print('The differece of square of the sum and the sum of the squares of the first {0} numbers is {1}'.format(value, difference(value)))