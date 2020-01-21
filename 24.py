"""
Finds mth lexicographic permutation of the first nth first digits 
Author: Juan Rios
"""
from math import factorial

def permutation_m(n,m):
    s = ''
    for i in range(n+1):
        s += str(i)
    solution = ''
    num = m
    coeff = n
    while (num>1):
        div = num//factorial(coeff)
        num = num%factorial(coeff)
        if (num==0):
            div-= 1
            num += factorial(coeff)
        solution += s[div]
        s = s[:div]+s[div+1:]
        coeff -= 1
    solution += s
    return solution

if __name__ == "__main__":
    m = 1
    n = 9
    print('The {0}th lexicographic permutation of the numbers from 0 to {1} is {2}'.format(m,n, permutation_m(n,m)))