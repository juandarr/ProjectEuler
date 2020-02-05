"""
Finds the maximum digital sum of values of the form a**b for a,b < 100
Author: Juan Rios
"""
import math

"""
Return maximum sum of digits for values of the form a**b for a,b < 100
"""
def max_digital_sum(limit_value):
    max_sum = 0
    for a in range(1,limit_value):
        for b in range(1,limit_value):
            suma = sum([int(i) for i in str(a**b)])
            if suma > max_sum:
                max_sum = suma
    return max_sum

    

if __name__ == "__main__":
    limit_value = 100
    print('The maximum digital sum of values a**b for a,b < {0} is {1}'.format(limit_value, max_digital_sum(limit_value)))