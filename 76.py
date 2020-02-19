"""
Finds all possible combinations of integers below value to generate value
Author: Juan Rios
"""
import math

"""
Calculate the possible number of partitions
"""
def find_partitions_dict(limit_value):
    p = {(1,1):0}
    for i in range(2,limit_value+1):
        tmp = 1
        index = 1
        while index<=(i-index):
            tmp += p[(i-index,index)]
            index += 1
        p[(i,1)]=tmp
        index = 2
        while index<=i:
            if index<=(i//2):
                p[(i,index)]= p[(i,index-1)]-p[(i-index+1,index-1)]
            else:
                p[(i,index)]= 1
            index += 1
    return p[(i,1)]

def find_partitions_array(limit_value):
    p = [[0]]
    for i in range(2,limit_value+1):
        tmp = 1
        for index in range(1,i//2+1):
            tmp += p[i-index-1][index-1]
        p.append([tmp])
        for index in range(2,i+1):
            if index<=(i//2):
                p[i-1].append(p[i-1][index-2]-p[i-index][index-2])
            else:
                for c in range(0,i-index+1):
                    p[i-1].append(1)
                break
    return p[i-1][0]

if __name__ == "__main__":
    limit_value = 100
    print('The total possible combination of integers to generate the value {0} is {1}'.format(limit_value,find_partitions_array(limit_value)))