"""
Finds the parameter D of the diophantine equation for which x is the largest , D<=1000
Author: Juan Rios
"""

import math

def get_sequence_period(i):
    sequence = [int(math.sqrt(i))]
    num = -sequence[-1]
    den = 1
    orig_num = -num
    orig_den = int(i-orig_num**2)
    start = True

    while True:
        num = -num
        den = int((i-num**2)/den)
        if [orig_num,orig_den]==[num,den] and not(start):
            return sequence
        # Finds the square root of the multiple of den that achieves the (num-den*mul)**2 closest to i
        mul = int(((2*num*den+math.sqrt(4*(num**2)*(den**2)-4*(den**2)*((num**2)-i)))/(2*(den**2))))
        sequence.append(mul)
        num = num-den*mul

        start = False
        
def continued_fractions(i):
    sequence = get_sequence_period(i)
    num_a = sequence[0]
    num_b = sequence[0]*sequence[1]+1 
    den_a = 1
    den_b = sequence[1]
    if len(sequence)==2:
        index = 1
    else: index = 2
    while True:
        if (num_b**2-i*den_b**2)==1:
            return (num_b, den_b)
        num_tmp = num_b
        num_b = num_b*sequence[index]+ num_a
        num_a = num_tmp

        den_tmp = den_b
        den_b = den_b*sequence[index]+ den_a
        den_a = den_tmp

        index += 1
        if index == len(sequence):
            index = 1

def get_max_x(limit_range):
    max_x = 0
    max_d = 0
    for d in range(1,limit_range+1):
        if math.sqrt(d)!=int(math.sqrt(d)):
            [x,y]= continued_fractions(d)
            if x > max_x:
                max_x = x
                max_d = d
    return max_d

if __name__ == "__main__":
    limit_range = 1000
    print('The D values D<={0} with the largest x value solution is {1}'.format(limit_range,get_max_x(limit_range)))