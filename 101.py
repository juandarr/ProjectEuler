"""
Finds the largest square formed by any member of a set of anagram pairs
Author: Juan Rios
"""
import math
import numpy as np

def solve_matrix_equation(A,b):
    """
    Solves matrix equation Ax=b using the inverse x= (A^-1)b
    """
    return A.I*b

def polynomial_fit(values,k_limit):
    approximations = []
    for k in range(1,k_limit+1):
        values_to_fit = values[:k]
        A = []
        for i in range(1,k+1):
            A.append([i**s for s in range(k)])
        b = []
        for i in values[:k]:
            b.append([i])
        A = np.matrix(A)
        b = np.matrix(b)
        x = solve_matrix_equation(A,b)
        tmp = []
        n = 1
        for i in range(0,len(values)):
            tmp.append(sum([x[i]*(i+1)**s for s in range(len(values))]))
        approximations.append(tmp)
    print(values, approximations)

if __name__ == "__main__":
    values = []
    for i in range(1,20):
        values.append(i**3)
    k_limit = 5
    print('The sum of the First incorrect term of BadOPs for the generator is {0}'.format(polynomial_fit(values,k_limit))) 