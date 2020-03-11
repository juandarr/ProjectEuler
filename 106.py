"""
Finds the number of tests required to guarantee that a given n element set is a special set sum
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

def is_matrix_unique(matrix):
    for idx1 in range(len(matrix)):
        candidates =[idx2 for idx2 in range(len(matrix)) if matrix[idx2][idx1]==1]
        best = None
        min_score = float('inf')
        for idx2 in candidates:
            if sum(matrix[idx2][idx1+1:])<min_score:
                min_score = sum(matrix[idx2][idx1+1:])
                best = idx2
        if best!=None:
            tmp = matrix[idx1]
            matrix[idx1]=matrix[idx2]
            matrix[idx2]=tmp
    for idx in range(len(matrix)):
        if matrix[idx][idx]==1:
            continue
        else:
            return False
    return True

def check_uniqueness(a,b):
    matrix_p =[]
    matrix_m =[]
    for i in a:
        matrix_p.append([])
        matrix_m.append([])
        for j in b:
            if i>j:
                matrix_p[-1].append(1)
            else:
                matrix_p[-1].append(0)
            if i<j:
                matrix_m[-1].append(1)
            else:
                matrix_m[-1].append(0)
    return is_matrix_unique(matrix_p) or is_matrix_unique(matrix_m)
    


def test_special_sets(filename):
    sets = read_sets(filename)
    total = 0
    for number_set in sets:
        #c = math.factorial(len(number_set))//(math.factorial(len(number_set)-2)*2)
        c = 0
        is_special = True
        ops = {}
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
                        
                        if (a,b) not in ops and (b,a) not in ops:
                            if len(comb)==len(comb2):
                                if not check_uniqueness(comb,comb2):
                                    c+=1
                            ops[(a,b)]=1
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
        print(number_set,c)
        if is_special:
            total += sum(number_set)
    return total

if __name__ == "__main__":
    filename = 'files/sets_test.txt'
    #m = [[[1,2],[3,4]],[[1,3],[2,4]],[[1,4],[2,3]]]
    #for el in m:
    #    print(el, check_uniqueness(el[0],el[1]))
    #print(is_matrix_unique([[0,1,0,0],[0,1,1,0],[1,0,1,0],[0,1,0,0]]))
    print('The sum of elements of all special sets is {0}'.format(test_special_sets(filename))) 