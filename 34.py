"""
Finds the sum of all curious numbers (numbers which are equal to the sum of the factorial of their digits)
Author: Juan Rios
"""
import math

"""
Calculate the sum of all curious numbers
"""
def curious_sum(factorials):
    total = 0
    for num in range(3,410000):
        val = sum([factorials[int(i)] for i in str(num)])
        if val==num:
            total += val
    return total

if __name__ == "__main__":
    factorials = []
    for i in range(10):
        factorials.append(math.factorial(i))
    print('The sum of curious numbers is {0}'.format(curious_sum(factorials))) 