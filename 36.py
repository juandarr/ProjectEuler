"""
Finds sum of numbers that are palindromic in base 10 and 2 under 1 million
Author: Juan Rios
"""
import math

# Converts decimal number to binary
def dec_2_bin(number):
    val = ''
    while (number != 1):
        val = str(number%2) + val
        number //= 2
    return '1'+val

# Finds the sum of palindromic values under 1 millon for base 10 and 2
def palindromic_sum(upper_limit):
    total = 0
    for i in range(1,1000000,2):
        val1 = str(i)
        if val1[-1]=='0':
            continue
        if val1==val1[::-1]:
            val2 = dec_2_bin(i)
            if val2[-1]=='0':
                continue
            if val2==val2[::-1]:
                total += i
    return total

if __name__ == "__main__":
    upper_limit = 10**6
    print('The sum of all palindromic values below {0} is {1}'.format(upper_limit,palindromic_sum(upper_limit))) 