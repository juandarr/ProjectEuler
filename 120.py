"""
Finds the sum of all residues of (a+1)^n+(a-1)^n % a^2
Author: Juan Rios
"""
import math

def explore_binomials(limit_n):
    '''
    returns the sum of maximum residues of (a+1)^n+(a-1)^n % a^2 for every a from 1 to limit_n
    '''
    r_total = 0
    for a in range(3,limit_n+1):
        if a%2==0:
            r_total+=a*(a-2)
        else:
            r_total += a*(a-1)
    return r_total

if __name__ == "__main__":
    limit_n = 1000
    print('The the sum of all residues of (a+1)^n+(a-1)^n % a^2 is {0}'.format(explore_binomials(limit_n)))