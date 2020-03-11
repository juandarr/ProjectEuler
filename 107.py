"""
Finds the number of triangles containing the origin in its interior
Author: Juan Rios
"""
import math
from itertools import combinations

def read_matrix(filename):
    """
    Reads matrix file
    """
    with open(filename) as matrix_file:
        matrix = matrix_file.read()
    matrix = matrix.split('\n')
    for idx in range(len(matrix)):
        coordinates = matrix[idx].split(',')
        points = []
        for i in range(len(coordinates)):
            if coordinates[i]=='-':
                points.append(0)
            else:
                points.append(int(coordinates[i]))
        matrix[idx] = points
    edges = []
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            if matrix[i][j]!=0:
                edges.append([(i,j),matrix[i][j]])
    return matrix,sorted(edges, key=lambda x: x[1], reverse = True)

def check_connection(matrix):
    all_connected = True
    links = {}
    for idx_r in range(len(matrix)):
        links[idx_r]=[i for i in range(len(matrix[idx_r])) if matrix[idx_r][i]!=0]
    for idx_r in range(len(matrix)):
        connection_test = set([i for i in range(len(matrix[idx_r]))])
        connected_to = set([idx_r]+links[idx_r])
        is_valid = True
        while True:
            tmp = connected_to
            for i in connected_to:
                connected_to=connected_to.union(set(links[i]))
            if connected_to==connection_test:
                break
            elif tmp==connected_to:
                is_valid = False
                break
        if not is_valid:
            return False
    return True

def take_sum(matrix):
    total = 0
    for idx_row in range(len(matrix)):
        total += sum(matrix[idx_row][idx_row+1:])
    return total

def minimize_network(filename):
    matrix, edges = read_matrix(filename)
    total1 = take_sum(matrix)
    for edge in edges:
        matrix[edge[0][0]][edge[0][1]]=0
        matrix[edge[0][1]][edge[0][0]]=0
        if check_connection(matrix):
            continue
        else:
            matrix[edge[0][0]][edge[0][1]]=edge[1]
            matrix[edge[0][1]][edge[0][0]]=edge[1]
            continue
    return total1-take_sum(matrix)

if __name__ == "__main__":
    filename = 'files/network.txt'
    print('The maximum saving by removing redundant edges is {0}'.format(minimize_network(filename))) 