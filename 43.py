"""
Finds the sum of all pandigital numbers with property of prime divisibility
Author: Juan Rios
"""

import math

"""
Calculate permutations of n elements in k positions
"""
def elements_perm_k(elements,k):
    perm = []
    n = len(elements)
    for i in elements:
        perm.append(i)
    while (k>1):
        tmp = []
        for i in perm:
            for j in elements:
                if str(j) not in i:
                    tmp.append(i+str(j))
        k -= 1
        perm = tmp
    return perm

# Returns the sum of 0-9 pandigitals with prime divisility in its digits
def pandigital_sum():
    perm10 = elements_perm_k('0123456789',10)
    print('Permutations ready!')
    total = 0
    for value in perm10:
        if value[5]=='5':        
            if value[3] in '02468':
                if int(value[2:5])%3==0:
                    if int(value[4:7])%7==0:
                        if int(value[5:8])%11==0:
                            if int(value[6:9])%13==0:
                                if int(value[7:10])%17==0:
                                    total += int(value)
                                    print(value)
    return total

if __name__ == "__main__":
    print('The sum of 0-9 pandigitals with prime divisibility is {0}'.format(pandigital_sum())) 