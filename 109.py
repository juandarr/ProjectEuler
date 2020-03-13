"""
Finds the number of distinct ways a player can checkout a score less than 100
Author: Juan Rios
"""
import math

def checkout_solutions(checkout,sequence,idx_sq,d):
    '''
    returns the number of solution for a given checkout value
    '''
    counter = 0
    for double in d:
        if double>checkout:
            break
        res = checkout-double

        if res==0:
            counter +=1
            continue
        if res<=60:
            if res in idx_sq:
                index = idx_sq[res]
            else:
                index = len(sequence)-1
                while res>sequence[index]:
                    index -=1
        else:
            index = len(sequence)-1

        for idx in range(index,-1,-1):
            a = sequence[idx]
            if a==res:
                counter+=1
                continue
            for idx2 in range(idx,-1,-1):
                if a+sequence[idx2]==res:
                    counter +=1
                elif a+sequence[idx2]<res:
                    break
    return counter


def darts_checkout(limit_value):
    s = [i for i in range(1,21)]+[25]
    d = [2*i for i in range(1,21)]+[50]
    t = [3*i for i in range(1,21)]
    sequence = sorted(s+d+t)
    idx_sq = {}
    for idx in range(len(sequence)-1):
        if sequence[idx]!=sequence[idx+1]:
            idx_sq[sequence[idx]]=idx
    idx_sq[sequence[-1]]=len(sequence)-1
    n = limit_value
    total  = 0
    for checkout in range(1,limit_value+1):
        total += checkout_solutions(checkout,sequence,idx_sq,d)
    return total

if __name__ == "__main__":
    limit_value=99
    print('The number of distinct ways a player can checkout a score less than 100 is {0}'.format(darts_checkout(limit_value))) 