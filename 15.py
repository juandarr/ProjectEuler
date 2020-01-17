"""
Finds the number of lattice paths for a given nxn grid
Author: Juan Rios
"""
import math

n = 20

"""
Recursive function - doesnt work for big grids
"""
def lattice_paths(i,j):
    if (j==n or i==n):
        return 1
    else:
       return (lattice_paths(i+1,j)+lattice_paths(i,j+1))

"""
This functions generates the solution using triangle numbers
"""
def triangle_grid_generation(n):
    ar = []
    ar.append([1])
    val = 1
    for i in range(2,n+2):
        val += i
        ar[0].append(val)
    for row in range(1,n-1):
        ar.append([1])
        val = 1
        for i in range(1,n+1):
            val += ar[row-1][i]
            ar[row].append(val)
    return (ar[-1][-1])

    
if __name__ == "__main__":
    print('The number of paths in a {0}x{0} grid are {1}'.format(n,triangle_grid_generation(n)))