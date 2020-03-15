"""
Finds the least number for which the proportion  of bouncy numbers is exactly 99%
Author: Juan Rios
"""
import math

def is_bouncy(num):
    '''
    returns True when the number is bouncy (not extrictly increasing or decreasing in its digits)
    '''
    idx = 0
    while (int(num[idx])==int(num[idx+1])):
        idx += 1
        if idx==len(num)-1:
            return False
    if int(num[idx])<int(num[idx+1]):
        increasing = True
    else:
        increasing = False
    for i in range(idx+1,len(num)-1):
        if int(num[i])<int(num[i+1]):
            if increasing:
                continue
            else:
                return True
        elif int(num[i])>int(num[i+1]):
            if not increasing:
                continue
            else:
                return True
    return False

def proportion(percentage):
    i = 101
    b = 0
    while True:
        if is_bouncy(str(i)):
            b += 1
        if b%percentage==0:
            if (b//percentage)*100==i:
                return i
        i+=1

if __name__ == "__main__":
    percentage = 99
    print('The least number for which the proportion  of bouncy numbers is exactly {0}% is {1}'.format(percentage,proportion(percentage))) 