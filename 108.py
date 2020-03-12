"""
Finds the least value of n for which the number of distinct solutions exceeds one thousand
Author: Juan Rios
"""
import math

def find_solution(n):
    y = n+1
    x = float('inf')
    solutions = 0
    while True:
        if n*y%(y-n)==0:
            x = n*y//(y-n)
            solutions += 1
        if x==y:
            break
        y+=1
    return solutions

def find_divisors(n):
    """
    Find divisors of n
    """
    div = []
    sqrt_n = int(math.sqrt(n))
    for d in range(1, sqrt_n+1):
        if n%d==0:
            if d**2==n:
                div.append(d)
            else:
                div.append(d)
                div.append(n//d) 
    div = sorted(div)
    '''
    sols = {}
    counter = 0
    for idx in range(len(div)):
        for i in div[idx+1:len(div)-idx]: 
            if i%div[idx]==0:
                m = div[idx]
                s = i//div[idx]
                k = n//(s*m)
                x = k*m*(m+s)
                y = k*s*(m+s)
                if (x,y) not in sols and (y,x) not in sols:
                    counter += 1
                    sols[(x,y)]=1
                    print(x,y,n,(x+y)*n==x*y)
    if math.sqrt(n)==int(math.sqrt(n)):
        counter +=1
    print(counter)
    '''
    return div


def explore_solutions():
    #65520
    #110880
    #120120
    n=180100
    c = 1
    while True:
        sols = find_solution(n)
        if sols>50*c:
            print(n,sols)
            c += 1
        if sols>1000:
            return n
        n += 1

if __name__ == "__main__":
    print('The least value of n exceeding 1 thousand distinct solutions is {0}'.format(explore_solutions())) 
    #n =120
    #print(find_divisors(n))
    #print(find_solution(n))