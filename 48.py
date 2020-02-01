"""
Finds the last ten digits of the sum 1**1+2**2+...+1000*1000
Author: Juan Rios
"""

"""
Returns last ten digits of the sum of powers
"""
def last_ten_digits_powers():
    val = 0
    for i in range(1, 1000+1):
        val += i**i
    return str(val)[-10:]

if __name__ == "__main__":
    print('The last ten digits of the sum of powers are {0}'.format(last_ten_digits_powers())) 