"""
Finds how many  times a laser beam hits internally an eliptic mirror before leaving
Author: Juan Rios
"""

import math
from time import time
from decimal import *
from utils import prime_factors,divisorGen
import numpy as np

"""
Finds how many  how many  times a laser beam hits internally an eliptic mirror before leaving
"""
def eliptic_mirror(x0,y0,x1,y1):
    contacts = 1
    while True:
        # Calculate the reflection angle from the normal to the surface and the incidence beam
        m_n = y1/(4*x1)
        b = y1-m_n*x1
        theta_n = math.atan(m_n)
        a = (x0-x1,y0-y1)
        norm_a = (a[0]**2+a[1]**2).sqrt()
        n = (-5,m_n*(x1-5)+b-y1)
        norm_n = (n[0]**2+n[1]**2).sqrt()
        theta_i = math.acos((n[0]*a[0]+n[1]*a[1])/(norm_a*norm_n))
        if (theta_i)*(180/math.pi)>90: 
            theta_r = math.pi+theta_n-theta_i
        elif (theta_i)*(180/math.pi)<-90:
            theta_r = math.pi+theta_n+theta_i
        elif (theta_n)*(180/math.pi)>90 or (theta_n)*(180/math.pi)<-90:
            print(theta_n,theta_i, theta_r)
            print('First ocurrence, what to do here? Theta n outside limits')
            break
        elif (theta_n+theta_i)*(180/math.pi)>90:
            print(theta_n*(180/math.pi),theta_i*(180/math.pi), theta_r*(180/math.pi))
            print('First ocurrence, what to do here? Sum bigger than limit')
            theta_r = 2*theta_n-theta_i-math.pi
        elif (theta_n+theta_i)*(180/math.pi)<-90:
            print(theta_n*(180/math.pi),theta_i*(180/math.pi), theta_r*(180/math.pi))
            print('First ocurrence, what to do here? Sum bigger than limit')
            theta_r = 2*theta_n+theta_i+math.pi
        else:
            theta_r = theta_n+theta_i
        m = Decimal(math.tan(theta_r))
        b = y1-Decimal(m)*x1
        print(theta_n,theta_i, theta_r,m,b)
        
        m2= m**2
        b2 =b**2
        
        x0_tmp = (-2*m*b+(4*m2*b2-4*(4+m2)*(b2-100)).sqrt())/(2*(4+m2))
        x1_tmp = (-2*m*b-(4*m2*b2-4*(4+m2)*(b2-100)).sqrt())/(2*(4+m2))
        y0_tmp = m*x0_tmp+b
        y1_tmp = m*x1_tmp+b
        print((round(x1,4),round(y1,4)),(round(x0_tmp,4),round(y0_tmp,4)),(round(x1_tmp,4),round(y1_tmp,4)))
        x0,y0 = (x1,y1)
        if round(x1,4)==round(x0_tmp,4):
            x1 = x1_tmp
            y1 = y1_tmp
        else:
            x1 = x0_tmp
            y1 = y0_tmp
        print('Contact {0}, New points:'.format(contacts),(x0,y0),(x1,y1))
        if x1>=-0.01 and x1<= 0.01:
            return contacts
        contacts+=1
        
# Wrong: 161

if __name__ == "__main__":
    print('The amount of times a laser beam hits internally an eliptic mirror before leaving is {0}'.format(eliptic_mirror(Decimal(0), Decimal(10.1),Decimal(1.4),Decimal(-9.6))))