"""
Finds the number of triangles containing the origin in its interior
Author: Juan Rios
"""
import math
from itertools import combinations

def read_sets(filename):
    """
    Reads sets file
    """
    with open(filename) as sets_file:
        sets = sets_file.read()
    sets = sets.split('\n')
    for idx in range(len(sets)):
        coordinates = sets[idx].split(',')
        points = []
        for i in range(len(coordinates)):
            points.append(int(coordinates[i]))
        sets[idx] = sorted(points)
    return sets

def test_special_sets(filename):
    sets = read_sets(filename)
    total = 0
    for number_set in sets:
        is_special = True
        for idx in range(len(number_set)-1):
            if number_set[idx]==number_set[idx+1]:
                is_special = False
                break
        if not is_special:
           continue
        for i in range(1,(len(number_set)//2)+1):
            options = [j for j in range(len(number_set))]
            for comb in combinations(options,i):
                a = 0
                complement = options.copy()
                for idx in comb:
                    a += number_set[idx]
                    complement.remove(idx)
                for j in range(max(i,2),len(complement)+1):
                    for comb2 in combinations(complement,j):
                        b = 0
                        for idx in comb2:
                            b += number_set[idx]
                        if a==b:
                            is_special=False
                            break
                        if i>j:
                            if a<b:
                                is_special = False
                                break
                        elif i<j:
                            if a>b:
                                is_special = False
                                break
                    if not is_special:
                        break
                if not is_special:
                    break
            if not is_special:
                break
        if is_special:
            total += sum(number_set)
    return total

if __name__ == "__main__":
    filename = 'files/sets.txt'
    print('The sum of elements of all special sets is {0}'.format(test_special_sets(filename))) 