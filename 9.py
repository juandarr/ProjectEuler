"""
Finds the product of the Pytagorean triplet for which a+b+c=1000
Author: Juan Rios
"""
import math

# Finds the product of the pythagorean triplet for which a+b+c=1000
def triplet_product():
    for b in range(498,2,-1):
        for a in range(b-1,1,-1):
            if ((1000*(a+b)-a*b)==(1000**2)/2):
                return a*b*(1000-a-b)

if __name__ == "__main__":
    print('The product of the pythagorean triplet for which a+b+c=1000 is {0}'.format(triplet_product()))