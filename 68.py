"""
Finds the maximum 16-digit string for a magic 5-gon ring
Author: Juan Rios
"""

import math
from itertools import permutations
        
def tuple_combinations(elements):
    tuple_combinations = []
    pairs = permutations(elements, r=2)
    for p in pairs:
        combinations = []
        for i in elements:
            if p[1]!=i and p[0]!=i:
                combinations.append([p[1],i])
        tuple_combinations.append((p,combinations))
    return tuple_combinations


def get_max_string():
    outer_ring_perm =  permutations([6,7,8,9,10])
    tuples_pairs = tuple_combinations([1,2,3,4,5])
    max_num = 0
    for outer in outer_ring_perm:
        visited = [-1,-1]
        set_inner = set()
        solution = True
        while len(set_inner)!=5:
            current_tuple = []
            set_inner = set()
            visited[1]=-1
            if visited[0]==19:
                solution = False
                break
            for index in range(2):
                diff = outer[2*index+1]-outer[2*index]
                for p_index in range(visited[index]+1,len(tuples_pairs)):
                    if current_tuple!=[]:
                        if current_tuple[-1][1]!=tuples_pairs[p_index][0][0] or tuples_pairs[p_index][0][1] in set_inner:
                            continue
                    found = False
                    visited[index] = p_index
                    for comb in tuples_pairs[p_index][1]:
                        if sum(tuples_pairs[p_index][0])-sum(comb)==diff:
                            if current_tuple!=[]:
                                if outer[0]+sum(current_tuple[0])!=outer[2]+sum(tuples_pairs[p_index][0]):
                                    continue
                            current_tuple.append(list(tuples_pairs[p_index][0]))
                            current_tuple.append(comb)
                            set_inner = set_inner.union(set(list(tuples_pairs[p_index][0])+comb))
                            found = True
                            break
                    if found:
                        break
        if solution:
            current_tuple.append([current_tuple[3][1],current_tuple[0][0]])
            if outer[0]+sum(current_tuple[0])==outer[4]+sum(current_tuple[-1]):
                index_min = outer.index(min(outer))
                index = index_min
                num = ''.join([''.join([str(i) for i in [outer[index%5]]+current_tuple[index%5]]) for index in range(index_min, index_min+len(outer))])
                if int(num)> max_num:
                    max_num = int(num)
    return max_num

if __name__ == "__main__":
    print('The maximum 16-digit string fro a magic 5-gon ring is {0}'.format(get_max_string()))