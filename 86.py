"""
Finds the least value of M that exceeds one million solutions (Shortest path integer)
Author: Juan Rios
"""
import math

"""
Calculates the cuboids with integers shortest distance to opposite corners
"""
def shortest_line_1st(limit_value):
    sol = 0
    square = {}
    counter = 0
    for i in range(1,100001):
        square[i]=i**2

    l = 1
    while sol<limit_value:
        for w in range(1,l+1):
            for h in range(w,l+1):
                counter += 1
                d = []
                if h!=w:
                    x = (l*square[h]-h*l*w)/(square[h]-square[w])
                    d.append(math.sqrt(square[w]+(l-x)**2)+math.sqrt(x**2+square[h]))
                    if h>w:
                        x = (l*square[h]+h*l*w)/(square[h]-square[w])
                        d.append(math.sqrt(square[w]+(l-x)**2)+math.sqrt(x**2+square[h]))
                else:
                    d.append(math.sqrt(square[w]+(l/2)**2)+math.sqrt((l/2)**2+square[h]))
                if l!=w:
                    x = (h*square[l]-l*h*w)/(square[l]-square[w])
                    d.append(math.sqrt(square[w]+(h-x)**2)+math.sqrt(x**2+square[l]))
                    x = (h*square[w]-w*h*l)/(square[w]-square[l])
                    d.append(math.sqrt(square[l]+(h-x)**2)+math.sqrt(x**2+square[w]))
                
                    if (l>w):
                        x = (h*square[l]+l*h*w)/(square[l]-square[w])
                        d.append(math.sqrt(square[w]+(h-x)**2)+math.sqrt(x**2+square[l]))
                        x = (h*square[w]+w*h*l)/(square[w]-square[l])
                        d.append(math.sqrt(square[l]+(h-x)**2)+math.sqrt(x**2+square[w]))
                else:
                    d.append(math.sqrt(square[w]+(h/2)**2)+math.sqrt((h/2)**2+square[l]))
                    d.append(math.sqrt(square[l]+(h/2)**2)+math.sqrt((h/2)**2+square[w]))
                d = min(d)
                if d.is_integer():
                    sol += 1
        l += 1
    return sol,l-1  

"""
Calculates the cuboids with integers shortest distance to opposite corners
"""
def shortest_line_sol(limit_value):
    sol = 0
    to_square = {}
    from_square = {}
    for i in range(1,10000):
        to_square[i]=i**2
        from_square[i**2]= i

    l = 1
    solved = {}
    threshold = 10000
    while sol<limit_value:
        for w in range(l,0,-1):
            for h in range(w,0,-1):
                if (l,w,h) not in solved:
                    ds = [to_square[w+h]+to_square[l],to_square[l+h]+to_square[w],to_square[w+l]+to_square[h]]
                    for index in range(len(ds)):
                        if ds[index] in from_square:
                            ds[index] = from_square[ds[index]]
                        else: 
                            ds[index] = math.sqrt(ds[index])
                    mini = min(ds)
                    if mini==int(mini):
                        factor=max(l,w,h)
                        for i in range(2,3000//factor):
                            solved[(i*l,i*w,i*h)] = 1
                        sol += 1
                else:
                    sol+=1
        l += 1
        if sol > threshold:
            print(l-1,sol)
            threshold += 10000
    return sol,l-1  

"""
Calculates the cuboids with integers shortest distance to opposite corners
"""
def shortest_line_optimized(limit_value):
    sol = 0
    to_square = {}
    from_square = {}
    for i in range(1,10000):
        to_square[i]=i**2
        from_square[i**2]= i

    l = 1
    solved = {}
    threshold = 10000
    while sol<limit_value:
        for w in range(l,0,-1):
            for h in range(w,0,-1):
                if (w+h,l) in solved: 
                    sol += 1
                else:
                    d = to_square[w+h]+to_square[l]
                    if d in from_square:
                        solved[(w+h,l)]=1
                        for i in range(2,2000//l):
                            solved[(i*(w+h),i*l)]=1
                        sol += 1
        l += 1
        if sol > threshold:
            print(l-1,sol)
            threshold += 10000
    return l-1  

if __name__ == "__main__":
    limit_value = 10**6
    print('The least value of m exceeding {0} solutions is {1}'.format(limit_value,shortest_line_optimized(limit_value)))