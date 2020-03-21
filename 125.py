"""
Finds the sum of all numbers less than limit_n that are both palindromic and the sum of consecutive squares
Author: Juan Rios
"""
import math

def palindromic_sum(limit_n,squares):
    '''
    returns the sum of all numbers less than limit_n that are both palindromic and the sum of consecutive squares
    '''
    total = 0
    visited = {}
    for i in range(1,int(math.sqrt(limit_n))+1):
        value = squares[i]
        for j in range(i+1,int(math.sqrt(limit_n))+1):
            value += squares[j]
            if value < limit_n:
                if str(value)==str(value)[::-1]:
                    if value not in visited:
                        total += value
                        visited[value]=1
                    else:
                        print('Value repeated: ', value)
            else:
                break
    return total
        

if __name__ == "__main__":
    limit_n = 10**8
    squares = {}
    for i in range(1,int(math.sqrt(limit_n))+1):
        squares[i]=i**2
    print('The sum of all numbers less than limit_n that are both palindromic and the sum of consecutive squares is {0}'.format(palindromic_sum(limit_n,squares)))