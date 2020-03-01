"""
Finds the number of right triangles to be placed in a n+1 dimensional grid
Author: Juan Rios
"""
import math

def find_factors(number):
    """
    Find pair of factors for a given number
    """
    factors = []
    for d in range(1,int(math.sqrt(number))+1):
        if number%d==0:
            factors.append([d,number//d])
    return factors

def right_triangle_counter(dimension):
    """
    Calculates the number of right triangles in a grid of dimension+1
    """
    squares = {}
    for i in range(1,dimension+1):
        squares[i**2]=i
    triangles = (dimension**2)*3
    
    for h in range(1,dimension+1):
        if h**2 in squares:
            factors = find_factors(h**2)
            for f in factors:
                if f[0]+f[1]<= dimension:
                    if f[0]==f[1]:
                        triangles += 2
                    else:
                        triangles += 4
    triangles += find_triangles(dimension)
    return triangles

def find_triangles(dimension):
    combs = 0
    points_stored = {}
    for x1 in range(1,dimension+1):
        for y1 in range(1,dimension+1):
            for x2 in range(1,dimension+1):
                for y2 in range(1,dimension+1):
                    c = (x2,y2)
                    a = (x1,y1)
                    if a==c:
                        continue
                    b = (x2-x1,y2-y1)
                    if a[0]*b[0]+a[1]*b[1]==0 or c[0]*b[0]+c[1]*b[1]==0:
                        if (a,c) not in points_stored:
                            if (c,a) not in points_stored:
                                points_stored[(a,c)] = 1
                                combs += 1
    return combs

if __name__ == "__main__":
    dimension = 50
    print('The number of right triangles in the {0}th  dimensional grid is {1}'.format(dimension,right_triangle_counter(dimension))) 