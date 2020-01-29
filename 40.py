"""
Product of a sequence of decimals in an irrational number which is  sequence of integers
Author: Juan Rios
"""

import math

# Product of a sequence of decimals in an irrational number 
def irrational_product(limit_power):
    product = 1
    i =1
    d = 1
    power =1
    num ='1'
    powers_10 = [10**i for i in range(1,limit_power+1)]
    index = 0
    while (True):
        div = 10**power
        while ((i+1)/div<1):
            i += 1
            d += power
            if index<len(powers_10):
                if (d/powers_10[index]>=1):
                    product *= int(str(i)[powers_10[index]-d-1])
                    index += 1
            else: break
        if index==len(powers_10):
            break
        power += 1
    return product

if __name__ == "__main__":
    limit_power = 6
    print('The product is {0}'.format(irrational_product(limit_power))) 