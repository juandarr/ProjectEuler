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
        cube = number**3
        cube_string = ''.join(sorted(str(cube))) 
        if cube_string not in visited:
            visited[cube_string]=1
            cubes = 1
            tmp_number = number+1
            cube_tmp_number = tmp_number**3
            while len(str(cube_tmp_number))==len(cube_string):
                if ''.join(sorted(str(cube_tmp_number)))==cube_string:
                    cubes += 1
                tmp_number += 1
                cube_tmp_number = tmp_number**3
            if cubes == cube_permutations:
                return cube
        number += 1

if __name__ == "__main__":
    cube_permutations = 5
    print('The smallest cube with {0} permutations that are also cubes is {1}'.format(cube_permutations, find_smallest_cube(cube_permutations)))