"""
Finds the passcode given a list of potential code positions
Author: Juan Rios
"""
import math
import numpy as np

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

def decimals_n_value(value, term):
    sequence = get_sequence_period(value)
    sequence = sequence + (sequence[1:])*(math.ceil(term/len(sequence[1:])))
    a_num = sequence[0]
    b_num = sequence[1]*sequence[0]+1

    a_den = 1
    b_den = sequence[1]
    #print(a_num, a_den)
    #print(b_num, b_den)
    for i in sequence[2:term]:
        tmp_num = b_num
        tmp_den = b_den
        b_num = b_num*i+a_num
        b_den = b_den*i+a_den
        a_num = tmp_num
        a_den = tmp_den
        #print(b_num, b_den)
    return b_num,b_den

def division(a,b):
    quot = a//b
    res = a%b
    q = [quot]
    while len(q)<100:
        if res<b:
            res *= 10
            while res<b:
                res *= 10
                q.append(0)
        if len(q)==100:
            break
        quot = res//b
        res = res%b
        q.append(quot)
        if res==0:
            break
    return q

if __name__ == "__main__":
    total = 0
    for i in range(2,100):
        if math.sqrt(i)!=int(math.sqrt(i)):
            a,b=decimals_n_value(i, 200)
            total += sum(division(a,b))
    print('The sum of the first 100 decimals of the first 100 square roots (if irrational) is {0}'.format(total))
#40760
#40928