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
        for i in range(0,len(values)):
            tmp.append(sum([round(x[idx,0])*(i+1)**idx for idx in range(len(x))]))
        approximations.append(tmp)
    total = 0
    for k in range(k_limit):
        for idx in range(len(approximations[k])):
            if approximations[k][idx]!=values[idx]:
                total += approximations[k][idx]
                break
    return int(total)
    
if __name__ == "__main__":
    values = []
    for i in range(1,20):
        values.append(1-i+i**2-i**3+i**4-i**5+i**6-i**7+i**8-i**9+i**10)
    k_limit = 11
    print('The sum of the First incorrect term of Bad OP (optimum polynomial) for the generator is {0}'.format(polynomial_fit(values,k_limit))) 