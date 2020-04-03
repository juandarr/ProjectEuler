"""
Finds the nth golden nugget of the equation Af(x)=g1*x+g2*x**2+..., where g1=1, g2=4
Author: Juan Rios
"""

import math
from time import time
from decimal import *

"""
Finds the nth golden nugget of the equation Af(x)=g1*x+g2*x**2+..., where g1=1, g2=4
"""
def golden_nuggets_modified(n_th):
    r = Decimal(5).sqrt()
    a = 9-4*r
    b = 9+4*r
    sols = []
    for n in range(n_th):
        s_ar = []
        s1 = -(-13*(a**n)+5*r*(a**n)-13*(b**n)-5*r*(b**n))
        s2 = (13*(a**n)+5*r*(a**n)+13*(b**n)-5*r*(b**n))
        s3 = -(-7*(a**n)+r*(a**n)-7*(b**n)-r*(b**n))
        s4 = (7*(a**n)+r*(a**n)+7*(b**n)-r*(b**n))
        s5 = -4*(a**n)+r*(a**n)-4*(b**n)-r*(b**n)
        s6 = 4*(a**n)+r*(a**n)+4*(b**n)-r*(b**n)
        s7 = -4*(a**n)-r*(a**n)-4*(b**n)-r*(b**n)
        s8 = 4*(a**n)-r*(a**n)+4*(b**n)+r*(b**n)
        #print(s1,s2,s3,s4,s5)
        for s in [s1,s2,s3,s4]:
            if round(s)%2==0 and round(s)>14:
                s_ar.append(round(s)//2)
        for s in [s5,s6,s7,s8]:
            if round(s)>7:
                s_ar.append(round(s))
        for s in s_ar:
            #print(s)
            if (s-7)%5==0:
                val = (s-7)//5
                sols.append(val)
    sols= sorted(sols)
    return sum(sols[:30])

if __name__ == "__main__":
    n_th = 11
    print('The sum of the {0} first golden nuggets of the equation Af(x)=g1*x+g2*x**2+... is {1}'.format(n_th,golden_nuggets_modified(n_th)))