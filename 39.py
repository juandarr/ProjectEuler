"""
Finds the perimeters p for which the number of solutions in a right angle triangle {a,b,c} is maximized
Author: Juan Rios
"""

import math

# Return value p that maximizes the number of solutions
def p_max_solutions(limit_perimeter):
    p_dict = {}
    p_value = 0
    p_max = 0
    for b in range(499,1,-1):
        for a in range(1,b):
            c = math.sqrt(a**2+b**2)
            if c > (limit_perimeter-b-a):
                continue
            if c==int(c):
                p = a+b+int(c)
                if p not in p_dict:
                    p_dict[p]=1
                else:
                    p_dict[p] += 1
                    if p_dict[p]>p_max:
                        p_max = p_dict[p]
                        p_value = p
    return p_value

    
if __name__ == "__main__":
    limit_perimeter = 1000
    print('The perimeter p that maximizes the number of solutions is {0}'.format(p_max_solutions(limit_perimeter))) 