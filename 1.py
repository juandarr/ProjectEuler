"""
Adds the multiples of 3 or 5 below a certain number
Author: Juan Rios
"""

def multiple_of_3_or_5(number):
    sum = 0
    for i in range(1,number):
        if (i%3==0 or i%5==0):
            sum += i
    return sum

if __name__ == "__main__":
    number = 1000
    print('The sum of multiples of 3 or 5 below {0} is {1}'.format(number, multiple_of_3_or_5(number)))