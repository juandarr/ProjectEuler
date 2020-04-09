"""
Finds how many  times a laser beam hits internally an eliptic mirror before leaving
Author: Juan Rios
"""

import math
from time import time
from decimal import *
from PIL import Image, ImageDraw

getcontext().prec =20

def pi():
    """Compute Pi to the current precision.

    >>> print(pi())
    3.141592653589793238462643383

    """
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s               # unary plus applies the new precision

"""
Finds how many  how many  times a laser beam hits internally an eliptic mirror before leaving
"""
def eliptic_mirror(x0,y0,x1,y1):
    contacts = 1
    limit =2
    frames = []
    im = Image.new('RGB', (400, 600), (255, 255, 255))
    draw = ImageDraw.Draw(im)

    draw.ellipse((100, 100, 300, 500), fill=(255, 255, 255), outline=(2, 2, 0))
    frames.append(im.copy())
    while True:
        draw.line((x0*20+200, -20*y0+300, 20*x1+200, -20*y1+300), fill=(255, 0, 0), width=1)

        if contacts==limit:
            frames.append(im.copy())
            limit+=1
        # Calculate the reflection angle from the normal to the surface and the incidence beam
        m_s = -4*x1/y1
        theta_s = Decimal(math.atan(m_s))

        m_i = (y0-y1)/(x0-x1)
        theta_i_ref = Decimal(math.atan(m_i))

        theta_r  = pi()+2*theta_s-theta_i_ref

        m = Decimal(math.tan(theta_r))

        b = y1-m*x1
        
        ms= m**2
        bs = b**2
        root = (4*ms*bs-4*(4+ms)*(bs-100)).sqrt()
        x0_tmp = (-2*m*b+root)/(2*(4+ms))
        x1_tmp = (-2*m*b-root)/(2*(4+ms))
        
        x0,y0 = (x1,y1)

        if abs(x1-x0_tmp)>=10**(-15):
            x1 = x0_tmp
        else:
            x1 = x1_tmp
        y1 = m*x1+b

        if abs(x1)<=0.01 and y1>0:
            im.show()
            # Save into a GIF file that loops forever
            frames[0].save('laser_beam.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)
            return contacts
        contacts+=1

if __name__ == "__main__":
    print('The amount of times a laser beam hits internally an eliptic mirror before leaving is {0}'.format(eliptic_mirror(Decimal(0), Decimal(10.1),Decimal(1.4),Decimal(-9.6))))