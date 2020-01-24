"""
Finds the sum of all the numbers that can be written as the sum of fifth power of their digits
Author: Juan Rios
"""

def sum_power(power,maximum_limit):
    sum_of_numbers = 0
    for i in range(maximum_limit,10,-1):
        total = 0
        for d in str(i):
            total += int(d)**power
            if total> i:
                break
        if total==i:
            sum_of_numbers += i
    return sum_of_numbers

if __name__ == "__main__":
    maximum_limit = 350000
    power = 5
    print('The sum of all numbers that can be written as sum of the {0}th power of its digits is {1}'.format(power,sum_power(power,maximum_limit)))