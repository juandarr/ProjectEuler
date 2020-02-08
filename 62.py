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

"""
Returns the smallest cube that has exactly 5 permutations that are also cubes
"""
def find_smallest_cube_alt(cube_permutations):
    visited= {}
    number = 345
    counter = 0
    min_value = float('inf')
    candidates = []
    while True:
        cube = number**3
        cube_string = ''.join(sorted(str(cube))) 
        if cube_string not in visited:
            visited[cube_string]=[cube,1]
        else:
            visited[cube_string][1]+=1
            if visited[cube_string][1]==cube_permutations:
                candidates.append(visited[cube_string][0])
                tmp_number = number+1
                cube_tmp_string = ''.join(sorted(str(tmp_number**3)))
                min_value = visited[cube_string][0]
                while len(cube_tmp_string)==len(cube_string):
                    if cube_tmp_string not in visited:
                        visited[cube_tmp_string]=[cube,1]
                    else:
                        visited[cube_tmp_string][1]+=1
                        if visited[cube_tmp_string][1]==cube_permutations:
                            if min_value > visited[cube_tmp_string][0]:
                                candidates.append(visited[cube_tmp_string][0])
                                print(candidates)
                                min_value = visited[cube_tmp_string][0]
                        elif visited[cube_tmp_string][0] in candidates:
                            candidates.remove(visited[cube_tmp_string][0])
                    tmp_number += 1
                    cube_tmp_string = ''.join(sorted(str(tmp_number**3)))
                return candidates[-1]
        number += 1

if __name__ == "__main__":
    cube_permutations = 6
    print('The smallest cube with {0} permutations that are also cubes is {1}'.format(cube_permutations, find_smallest_cube_alt(cube_permutations)))