"""
Finds the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 to 9 pandigital
Author: Juan Rios
"""
import math

"""
Calculate permutations of n elements in k positions
"""
def n_perm_k(n,k):
    perm = []
    for i in range(1, n+1):
        perm.append(str(i))
    while (k>1):
        tmp = []
        for i in perm:
            for j in range(1,n+1):
                if str(j) not in i:
                    tmp.append(i+str(j))
        k -= 1
        perm = tmp
    return perm


"""
Calculate the sum of pandigital numbers
"""
def total_pandigital():
    perm_1 = n_perm_k(9,1)
    perm_2 = n_perm_k(9,2)
    perm_3 = n_perm_k(9,3)
    perm_4 = n_perm_k(9,4)
    total = 0
    vals = {}
    for num in perm_4:
        for div in perm_2:
            val = int(num)
            div_val = int(div)
            if val%div_val==0:
                if str(val//div_val) in perm_3:
                    if set(str(val//div_val)+num+div)=={'1','2','3','4','5','6','7','8','9'}:
                        if val not in vals:
                            print((val//div_val), div, val)
                            total += val
                            vals[val] = 1
        for div in perm_1:
            val = int(num)
            div_val = int(div)
            if val%div_val==0:
                if str(val//div_val) in perm_4:
                    if set(str(val//div_val)+num+div)=={'1','2','3','4','5','6','7','8','9'}:
                        if val not in vals:
                            print((val//div_val), div, val)
                            total += val
                            vals[val] = 1
    return total

if __name__ == "__main__":
    print('The sum of all the products is {0}'.format(total_pandigital())) 
