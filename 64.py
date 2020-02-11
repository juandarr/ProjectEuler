"""
Finds the number of continued fractions sqrt(N) for N <= 10000 with an odd period
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
            return len(sequence[1:])
        # Finds the square root of the multiple of den that achieves the (num-den*mul)**2 closest to i
        mul = int(((2*num*den+math.sqrt(4*(num**2)*(den**2)-4*(den**2)*((num**2)-i)))/(2*(den**2))))
        sequence.append(mul)
        num = num-den*mul

        start = False
        
"""
Returns the number of continued fractions sqrt(N) for N <= 10000 with an odd period
"""
def continued_fractions_odd(limit_range):
    counter = 0
    for i in range(2,limit_range+1):
        if math.sqrt(i)!=int(math.sqrt(i)):
            if get_sequence_period_numeric(i)%2==1:
                counter += 1
    return counter
    
if __name__ == "__main__":
    limit_range = 10000
    print('The number of continued fractions sqrt(N) for N <= {0} with an odd period is {1}'.format(limit_range, continued_fractions_odd(limit_range)))