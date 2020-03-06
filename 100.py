"""
Finds the number of blue discs for arrangements of discs of over 10**12 with a probability of 50% of taking two blue discs
Author: Juan Rios
"""
import math
from itertools import combinations

def find_probability(initial_value):
    i = initial_value
    while True:
        if i%2==1:
            squared = 1+2*(i**2-1)
            root = math.sqrt(squared)
            if int(root+0.5)**2==squared:
                return squared
        i += 1
        print(i)
        #print(i)

if __name__ == "__main__":
    initial_value = int(math.sqrt(2*(10**24)-2*10**12+1))+1
    print('The first arrangement of over {0} discs with a probability of 50% of taking two blue discs is {1}'.format(initial_value, find_probability(initial_value))) 