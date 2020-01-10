"""
Adds the even valued numbers of the fibonacci series below limit
Author: Juan Rios
"""

def fibonacci_sum(limit):
    a = 1
    b = 2
    sum = 0
    while (b<limit):
        if (b%2==0):
            sum += b
        temp = b
        b += a
        a = temp
    return sum

if __name__ == "__main__":
    limit = 4000000
    print('The sum of even-valued fibonnaci terms below {0} is {1}'.format(limit, fibonacci_sum(limit)))