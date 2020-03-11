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
    for idx_r in range(len(matrix)):
        connection_test = set([i for i in range(len(matrix)) if i!=idx_r])
        connected_to = set([i for i in matrix[idx_r] if i!=0])
    pass

def minimize_network(filename):
    matrix, edges = read_matrix(filename)
    print(matrix[0][:10], len(edges), edges)

    pass

if __name__ == "__main__":
    #filename = 'files/network.txt'
    filename = 'files/network_test.txt'
    print('The maximum saving by removing redundant edges is {0}'.format(minimize_network(filename))) 