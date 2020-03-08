"""
Finds the largest square formed by any member of a set of anagram pairs
Author: Juan Rios
"""
import math
from itertools import combinations

def read_triangle_points(filename):
    """
    Reads triangle points file
    """
    with open(filename) as triangles_file:
        triangles = triangles_file.read()
    triangles = triangles.split('\n')
    for idx in range(len(triangles)):
        coordinates = triangles[idx].split(',')
        points = []
        for i in range(0,len(coordinates),2):
            points.append([int(coordinates[i]),int(coordinates[i+1])])
        triangles[idx] = points
    return triangles

def contains_origin_checker(filename):
    triangles = read_triangle_points(filename)
    total = 0
    for t in triangles:
        #0: x negative, 1: x positive, 2: y negative, 3: y positive
        intercept_axis=[False, False, False, False] 
        origin_contained = False
        for side in combinations([0,1,2],2):
            if t[side[0]][0]!=t[side[1]][0] and t[side[0]][1]!=t[side[1]][1]:
                m = (t[side[0]][1]-t[side[1]][1])/(t[side[0]][0]-t[side[1]][0])
                b = t[side[0]][1]-m*t[side[0]][0]
                y_limits = sorted([t[side[0]][1],t[side[1]][1]])
                x_limits = sorted([t[side[0]][0],t[side[1]][0]])
                if b<=y_limits[1] and b>=y_limits[0]:
                    if b > 0 and b<=y_limits[1] and b>=y_limits[0]:
                        intercept_axis[3]=True
                    elif b <0:
                        intercept_axis[2]=True
                x_i = -b/m
                if x_i<=x_limits[1] and x_i>=x_limits[0]:
                    if x_i > 0:
                        intercept_axis[1]=True
                    elif x_i <0:
                        intercept_axis[0]=True
            elif t[side[0]][1]==t[side[1]][1]:
                b = t[side[0]][1]
                if b<=y_limits[1] and b>=y_limits[0]:
                    if b > 0:
                        intercept_axis[3]=True
                    elif b <0:
                        intercept_axis[2]=True
            elif t[side[0]][0]==t[side[1]][0]:
                x_i = t[side[0]][0]
                if x_i<=x_limits[1] and x_i>=x_limits[0]:
                    if x_i > 0:
                        intercept_axis[1]=True
                    elif x_i <0:
                        intercept_axis[0]=True
            if intercept_axis==[True]*4:
                origin_contained = True
                break
        if origin_contained:
            total += 1
    return total
    
if __name__ == "__main__":
    filename = 'files/p102_triangles.txt'
    print('The number of triangles containing the origin inside them is {0}'.format(contains_origin_checker(filename))) 