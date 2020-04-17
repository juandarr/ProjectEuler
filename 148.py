"""
Finds the number of entries with numbers multiple of 7 in the pascal's  triangle
Author: Juan Rios
"""

import math
from time import time
from utils import prime_factors

"""
Finds the number of entries with numbers multiple of 7 in the pascal's  triangle
"""
def pascal_multiple_seven(limit_row):
    prev_row=[1,1]
    total = 3
    sequence = [1,2]
    for r_idx in range(2,limit_row+1):
        partial  = 2
        row = [1]
        for col in range(r_idx-1):
            val = prev_row[col]+prev_row[col+1]
            row.append(val)
            if val%7!=0:
                partial += 1
        sequence.append(partial)
        row.append(1)
        prev_row = row
        total += partial
    return total,sequence

"""
Finds the number of entries with numbers multiple of 7 in the pascal's  triangle
"""
def pascal_multiple_seven_alt(limit_row):
    value_test,sequence = pascal_multiple_seven(limit_row)
    skip_row = 1
    rows_to_skip={}
    while skip_row<=limit_row:
        skip_row *= 7
        rows_to_skip[skip_row]=1
    #print(rows_to_skip)
    row = 0
    total = 0
    base = 1
    inc = 1
    step = 1
    transition =  1
    power = 7*7
    idx = 0
    counter =1
    acum = 1
    while row<=limit_row:
        start = step
        inc = start
        for i in range(7):
            print('New batch: {0} to {1}. {2}x{3}'.format(row,row+6, base,inc))
            if base==sequence[idx]:
                print('Success')
            else:
                print('Fail', base, sequence[idx])
            idx+=1
            for j in range(7):
                if row in rows_to_skip:
                    row += 1
                    total += 2
                    continue
                if row>limit_row:
                    return total
                total += base+j*inc
                #print(row, base+j*inc)
                row += 1
            base += step
            inc =  base
        #print(base-step)
        if ((base-step)%(counter*power))==0:
            quot = ((base-step)//(power))
            counter += 1
            if quot==7:
                counter = 1
                transition = 1
                power += power
                acum = 1
                print('Power is changed!')
            else:
                acum += 1
            print('Changes here!')
            transition += acum
            step = transition
            base = transition
            inc = transition
            #print('Here things change: ', transition, base, step)
            continue
        step += transition
        base = step
        inc = step

# Wrong: 93294484786211968
if __name__ == "__main__":
    limit_row=int(3*10**3-1)
    print('The number of entries with numbers multiple of 7 in the pascal triangle in the first {0} rows is {1}'.format(limit_row+1,pascal_multiple_seven_alt(limit_row)))