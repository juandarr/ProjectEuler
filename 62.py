"""
Finds the smallest cube that has exactly 5 permutations that are also cubes
Author: Juan Rios
"""

import math
from utils import elements_perm_k
from itertools import permutations

"""
Returns the smallest cube that has exactly 5 permutations that are also cubes
"""
def find_smallest_cube(cube_permutations):
    visited= {}
    number = 345
    while True:
        print(number)
        cube = number**3
        cube_string = str(cube)
        if cube_string not in visited:
            candidates = set([''.join(p) for p in permutations(cube_string)])
            cubes = 0
            for candidate in candidates:
                visited[candidate]=1
                cr = int(candidate)**(1/3)
                if abs(cr-math.ceil(cr))<10**(-10):
                    cubes += 1
            if cubes == cube_permutations:
                return cube
        number += 1

if __name__ == "__main__":
    cube_permutations = 5
    print('The smallest cube with {0} permutations that are also cubes is {1}'.format(cube_permutations, find_smallest_cube(cube_permutations)))