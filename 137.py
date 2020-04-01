"""
Finds the nth golden nugget of the equation Af(x)=f1*x+f2*x**2+...
Author: Juan Rios
"""

import math
from time import time

"""
Finds the golden nuggets of the equation
"""
def golden_nuggets(n_th):
    r = math.sqrt(5)
    a = 9-4*r
    b = 9+4*r
    sols = []
    for n in range(12):
        s1 = -0.5*(-(a**n)+r*(a**n)-b**n-r*b**n)
        s2 = -0.5*((a**n)+r*(a**n)+b**n-r*b**n)
        s3 = 2*a**n+r*a**n+2*b**n-r*b**n
        s4 = -2*a**n-r*a**n-2*b**n+r*b**n
        for s in [s1,s2,s3,s4]:
            val = (int(s)-1)/5
            if val>0 and val ==int(val):
                sols.append(int(val))
    sols= sorted(sols)
    return sols[n_th-1]

if __name__ == "__main__":
    n_th = 15
    print('The {0}th golden nugget of the equation Af(x)=f1*x+f2*x**2+... is {1}'.format(n_th,golden_nuggets(n_th)))