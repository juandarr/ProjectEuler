"""
Finds the minimum differrence of a pair of pentagonal numbers
Author: Juan Rios
"""

import math

"""
Return the minimum different of the pair of pentagonal numbers
"""
def minimum_difference(p):
    d = 10**7
    for i in range(len(p)-1):
        if p[i+1]-p[i]>d:
            print('Found the limit, this is definitely the minimum!')
            return d
        for j in range(i+1, len(p)):
            tmp = p[j]-p[i]
            if tmp<d:
                n1 = (0.5+math.sqrt(0.5**2+6*tmp))/3
                if n1==int(n1):
                    tmp_plus = p[j]+p[i]
                    n2 = (0.5+math.sqrt(0.5**2+6*tmp_plus))/3
                    if n2==int(n2):
                        d = tmp
            else:
                break
    return d

if __name__ == "__main__":
    p =[]
    # It should go until limit 10**7 to guarantee the value d is the minimum
    index_limit = 3000
    for i in range(1,index_limit+1):
        p.append((i*(3*i-1))//2)
    print('The minimum difference of two pentagonal numbers is {0}'.format(minimum_difference(p))) 