"""
Finds the first 10 digits of the sum of 100 50-digit numbers
Author: Juan Rios
"""
import math

def collatz_sequence(maximum_limit):
    max_counter = 0
    max_value = 0
    sequence_length = {}
    for i in range(2, maximum_limit):
        counter = 1
        num = i
        while (num > 1):
            if (num%2==0):
                num //= 2
            else:
                num = 3*num + 1
            counter += 1
            if num in sequence_length:
                counter += sequence_length[num]
                break
        sequence_length[i] = counter
        if counter > max_counter:
            max_counter = counter
            max_value = i
    return max_value

if __name__ == "__main__":
    maximum_limit = 10**6
    print('The number below {0} with the longest collatz sequence is {1}'.format(maximum_limit,collatz_sequence(maximum_limit)))