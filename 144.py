"""
Finds how many  times a laser beam hits internally an eliptic mirror before leaving
Author: Juan Rios
"""

import math
from time import time
from decimal import *
from utils import prime_factors,divisorGen
import numpy as np
from PIL import Image, ImageDraw
from time import time
from IPython.display import clear_output


im = Image.new('RGB', (200, 300), (255, 255, 255))
draw = ImageDraw.Draw(im)

draw.ellipse((50, 50, 150, 250), fill=(255, 255, 255), outline=(2, 2, 0))

"""
Finds how many  how many  times a laser beam hits internally an eliptic mirror before leaving
"""
def eliptic_mirror(x0,y0,x1,y1):
    contacts = 1
    limit =2

    while True:
        
        draw.line((x0*10+100, -10*y0+150, 10*x1+100, -10*y1+150), fill=(255, 0, 0), width=1)
        t0 = time()
        if contacts==limit:  
            im.show()
            print(contacts)
            limit+=1
            while time()-t0<2:
                continue
    
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
            theta_i = -theta_i+math.pi
            theta_r = theta_n+theta_i 
        elif (theta_i)*(180/math.pi)<90:
            theta_i = math.pi +theta_i
            theta_r = theta_n+theta_i
        #elif ((theta_n)*(180/math.pi)>0 and (theta_i)*(180/math.pi)>90) or ((theta_n)*(180/math.pi)>0 and (theta_i)*(180/math.pi)<90):
        #    theta_r = theta_n-theta_i
        else:
            theta_r = theta_n+theta_i

        '''
        if ((theta_n)*(180/math.pi)<0 and (theta_i)*(180/math.pi)>90) or ((theta_n)*(180/math.pi)<0 and (theta_i)*(180/math.pi)<90):
            theta_r = math.pi+theta_n-theta_i
        elif ((theta_n)*(180/math.pi)>0 and (theta_i)*(180/math.pi)>90) or ((theta_n)*(180/math.pi)>0 and (theta_i)*(180/math.pi)<90):
            theta_r = theta_n-theta_i
        else:
            theta_r = theta_n+theta_i
        '''
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
        if round(x1,5)==round(x0_tmp,5):
            x1 = x1_tmp
            y1 = y1_tmp
        else:
            x1 = x0_tmp
            y1 = y0_tmp
        if x1>=-0.01 and x1<= 0.01:
            return contacts
        contacts+=1
        print('Contact {0}, New points:'.format(contacts),(round(x0,4),round(y0,4)),(round(x1,4),round(y1,4)))
        
        
        
# Wrong: 161
# Wrong: 274
# Wrong: 275
# Wrong: 162

if __name__ == "__main__":
    print('The amount of times a laser beam hits internally an eliptic mirror before leaving is {0}'.format(eliptic_mirror(Decimal(0), Decimal(10.1),Decimal(1.4),Decimal(-9.6))))