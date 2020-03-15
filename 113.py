"""
Finds the amount of numbers below a googol that are not bouncy
Author: Juan Rios
"""
import math

def non_bouncy_generator(power):
    '''
    returns the amount of numbers below a googol that are not bouncy
    '''
    ascending = []
    descending = []
    neutral = []
    n = 0
    neutral.append([str(i) for i in range(1,10)])
    ascending.append([])
    descending.append([])
    n+=1
    digits = [str(i) for i in range(10)]
    while n<power:
        neutral.append([])
        ascending.append([])
        descending.append([])
        visited = {}
        for asc in ascending[n-1]:
            for i in digits[::-1]:
                if int(i)>=int(asc[-1]):
                    if asc+i not in visited:
                        ascending[n].append(asc+i)
                        visited[asc+i]=1
                else:
                    break
            for i in digits:
                if int(i)<=int(asc[0]):
                    if i+asc not in visited and i!='0':
                        ascending[n].append(i+asc)
                        visited[i+asc]=1
                else:
                    break
        
        for neu in neutral[n-1]:
            for i in digits:
                if i+neu not in visited and i!='0':
                    if int(i)<int(neu[0]):
                        ascending[n].append(i+neu)
                        visited[i+neu]=1
                    elif int(i)==int(neu[0]):
                        neutral[n].append(i+neu)
                        visited[i+neu]=1
                    else:
                        descending[n].append(i+neu)
                        visited[i+neu]=1
                if neu+i not in visited:
                    if int(i)>int(neu[-1]):
                        ascending[n].append(neu+i)
                        visited[neu+i]=1
                    elif int(i)<int(neu[-1]):
                        descending[n].append(neu+i)
                        visited[neu+i]=1
        
        for dsc in descending[n-1]:
            for i in digits:
                if int(i)<=int(dsc[-1]):
                    if dsc+i not in visited:
                        descending[n].append(dsc+i)
                        visited[dsc+i]=1
                else:
                    break
            for i in digits[::-1]:
                if int(i)>=int(dsc[0]):
                    if i+dsc not in visited and i!='0':
                        descending[n].append(i+dsc)
                        visited[i+dsc]=1
                else:
                    break
        n+=1
    total = 0
    for i in neutral:
        total += len(i)
    for i in ascending:
        total += len(i)
    for i in descending:
        total += len(i)
    return total

if __name__ == "__main__":
    power = 14
    print('The amount of numbers below a googol that are not bouncy is {0}'.format(non_bouncy_generator(power)))
     