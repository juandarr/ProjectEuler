"""
Finds the first 1000-digit in the Fibonacci series
Author: Juan Rios
"""

def fibonacci(number_length):
    a = 1 
    b = 1
    current_index = 2
    big_number = 10**(number_length-1)
    while ((b/big_number)<1):
        tmp = b
        b = a + b
        a = tmp
        current_index += 1
    return current_index
    
if __name__ == "__main__":
    number_length = 1000
    print('The first fibonacci term with {0} digits is the one at index {1}'.format(number_length, fibonacci(number_length)))