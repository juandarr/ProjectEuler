"""
Finds the number of continued fractions sqrt(N) for N <= 10000 with an odd period
Author: Juan Rios
"""

import math

def get_sequence_period(i):
    sequence = [int(math.sqrt(i))]
    num = -sequence[-1]
    den = 1
    orig_num = sequence[-1]
    orig_den = i-orig_num**2
    start = True

    while True:
        num = -num
        den = int((i-num**2)/den)
        
        if [orig_num,orig_den]==[num,den] and not(start):
            print(i, len(sequence[1:]))
            return len(sequence[1:])

        mul=[j for j in range(1,i//den+1) if (num-den*j)**2<i][-1]
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
            if get_sequence_period(i)%2==1:
                counter += 1
    return counter
    
if __name__ == "__main__":
    limit_range = 10000
    '''
    for i in range(2,21):
        if math.sqrt(i)!=int(math.sqrt(i)):
            print(i)
            get_sequence_period(i)
    '''
    print('The number of continued fractions sqrt(N) for N <= {0} with an odd period is {1}'.format(limit_range, continued_fractions_odd(limit_range)))