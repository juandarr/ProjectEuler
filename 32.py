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
def total_pandigital_less():
    perm_1 = n_perm_k(9,1)
    perm_2 = n_perm_k(9,2)
    
    perm_3 = n_perm_k(9,3)
    perm_3_index = [0]*(int(perm_3[-1])+1)
    for i in perm_3:
        perm_3_index[int(i)]=1

    perm_4 = n_perm_k(9,4)
    perm_4_index = [0]*(int(perm_4[-1])+1)
    for i in perm_4:
        perm_4_index[int(i)]=1

    total = set()
    operations = 0
    for num1 in perm_3:
        for num2 in perm_2:
            operations += 1
            prod = int(num1)*int(num2)
            if prod < len(perm_4_index):
                if perm_4_index[prod]==1:
                    if set(num1+num2+str(prod))=={'1','2','3','4','5','6','7','8','9'}:
                                total.add(prod)
    for num1 in perm_4:
        for num2 in perm_1:
            operations += 1
            prod = int(num1)*int(num2)
            if prod < len(perm_4_index):
                if perm_4_index[prod]==1:
                    if set(num1+num2+str(prod))=={'1','2','3','4','5','6','7','8','9'}:
                                total.add(prod)
        
    return operations ,sum(total)

if __name__ == "__main__":
    print('The sum of all the products is {0}'.format(total_pandigital_less())) 
