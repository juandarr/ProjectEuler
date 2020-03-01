"""
Finds how many numbers below 10 million arrive at 89
Author: Juan Rios
"""
import math

def chain_counter(limit_value):
    i = 1
    counter=0
    squares ={}
    for i in range(10):
        squares[str(i)]=i**2
    shortcut = {}

    while i < limit_value:
        num = i
        while True:
            if num in shortcut:
                num = shortcut[num]
                if num==89:
                    counter+=1
                break
            else:
                num = sum([squares[i] for i in str(num)])
                if num ==89:
                    counter+=1
                    break
                elif num==1:
                    break
        if i<568:
            shortcut[i] = num
        if i%10**6==0:
            print(i,counter)
        i+=1
    return counter

if __name__ == "__main__":
    limit_value = 10**7
    print('The amount of numbers below {0}  ending at 89 is {1}'.format(limit_value,chain_counter(limit_value))) 