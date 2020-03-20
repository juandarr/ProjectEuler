"""
Finds the sum of all minimum number of multiplications to compute n^k for k>=1 and k<=200
Author: Juan Rios
"""
import math

def minimum_products(limit_n):
    '''
    returns the sum of all minimum number of multiplications to compute n^k for k>=1 and k<=200
    '''
    ar = [[1]]
    k = [i for i in range(2,limit_n+1)]
    m = {}
    for val in k:
        m[val]=float('inf')
    l = 1
    mini = 0
    while len(k)>0:
        tmp = []
        for i in ar:
            pivot = i[-1]
            completed = False
            for j in i[::-1]:
                tmp.append(i+[pivot+j])
                if pivot+j<=limit_n:
                    if m[pivot+j]>l:
                        m[pivot+j]=l
                        k.remove(pivot+j)
                        if len(k)==0:
                            completed = True
                            break
            if completed:
                break
        l +=1
        ar = tmp
    total = 0
    for key in m:
        total += m[key]
    return total

# Wrong: 1781
if __name__ == "__main__":
    limit_n = 200
    print('The sum of all minimum number of multiplications to compute n^k for k>=1 and k<=200 is {0}'.format(minimum_products(limit_n)))