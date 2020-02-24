"""
Finds nearest area containing close to 2 million rectangles 
Author: Juan Rios
"""
import math

"""
Calculates the number of rectangles in a l*h grid
"""
def rectangle_counter(l,h):
    total = 0
    for ls in range(1,l+1):
        for hs in range(1,h+1):
            total += (l-ls+1)*(h-hs+1)
    return total 

"""
Calculate the dimension of the square with number of rectangles close to limit_value
"""
def squared_area(limit_value):
    i = 1
    delta = float('inf')
    total = 0
    while delta>abs(limit_value-total):
        total_prev = total
        delta = abs(limit_value-total_prev)
        total = rectangle_counter(i,i)
        i += 1
    return i-2

def rectangled_area(limit_value):
    minimum = float('inf')
    area = None
    l_local = None
    h_local = None
    # boundaries have been defined empirically, trying with different values and setting 
    # limits given the areas closest to having 2 million rectangles
    for x in range(1,2001):
        for y in range(x,2000-x+2):
            if x*y>2900 or x*y<2000:
                continue 
            total = rectangle_counter(x, y)
            if abs(limit_value-total)<minimum:
                minimum = abs(limit_value-total)
                l_local = x
                h_local = y
                area = x*y
    return area
        
if __name__ == "__main__":
    limit_value = 2*10**6
    print('The nearest area containing close to {0} rectangles is {1}'.format(limit_value,rectangled_area(limit_value)))