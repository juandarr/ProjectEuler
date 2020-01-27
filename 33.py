"""
Finds the product of denominators of the list of non trivial curious fractions in its lowest common terms
Author: Juan Rios
"""
import math

"""
Calculate the product of denominators of non trivial curious fractions in its lowest common terms
"""
def curious_fraction():
    num_product = 1
    den_product = 1
    for i in range(11,100):
        n1 = str(i)
        for j in range(i+1,100):
            n2 = str(j)
            if i!=j:
                for index in range(len(n1)):
                    if n1[index] in n2 and n1[index]!='0':
                        rem_index = n2.index(n1[index])
                        tmp1 = int(n1[:index]+n1[index+1:])
                        tmp2 = int(n2[:rem_index]+n2[rem_index+1:])
                        if tmp2!=0:
                            if int(n1)/int(n2)==tmp1/tmp2:
                                if tmp2%tmp1==0:
                                    tmp2 //= tmp1
                                    tmp1 = 1
                                num_product *= tmp1
                                den_product *= tmp2
    return den_product//num_product

if __name__ == "__main__":
    print('The product of denominators of non trivial curious numbers is {0}'.format(curious_fraction())) 