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
def pascal_multiple_seven_tests(limit_row):
    prev_row=[1,1]
    total = 3
    sequence = [1,2]
    counter = 2
    for r_idx in range(2,limit_row+1):
        partial  = 2
        row = [1]
        for col in range(r_idx-1):
            val = prev_row[col]+prev_row[col+1]
            row.append(val)
            if val%7!=0:
                partial += 1
        sequence.append(partial)
        counter +=1
        if counter==49:
            print(sequence[len(sequence)-49:], r_idx)
            counter = 0
        row.append(1)
        prev_row = row
        total += partial
    return 0
    #return total,sequence

"""
Finds the number of entries with numbers multiple of 7 in the pascal's  triangle
"""
def pascal_multiple_seven(limit_row):
    prev_row=[0]*10**6
    prev_row[0]=1
    prev_row[1]=1
    total = 3
    #sequence = [1,2]
    for r_idx in range(2,limit_row+1):
        partial  = 2
        tmp = 1
        for col in range(r_idx-1):
            tmp2 = prev_row[col+1]
            prev_row[col+1] = tmp+prev_row[col+1]
            tmp = tmp2
            if prev_row[col+1]%7!=0:
                partial += 1
        prev_row[r_idx]=1
        #sequence.append(partial)
        total += partial
    return total

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
    step = 1
    transition =  1

    power = 7*7
    idx = 0
    counter =1

    while row<=limit_row:
        for i in range(7):
            print('New batch: {0} to {1}. {2}'.format(row,row+6, base))
            if base==sequence[idx]:
                print('Success')
            else:
                print('Fail', base, sequence[idx])
            idx+=1
            for j in range(1,8):
                if row in rows_to_skip:
                    row += 1
                    total += 2
                    continue
                if row>limit_row:
                    return total
                total += j*base
                #print(row, base+j*inc)
                row += 1
            base += step
        print(base-step, counter, power)
        if ((base-step)%(counter*power))==0:
            counter+=1
            if counter>7:
                step = 1
                base = 1
                power *=7
                counter = 1
            print('Changes here!')
        step += step
        base = step

def value_generator(limit_row):
    #value_test,sequence = pascal_multiple_seven(limit_row)
    skip_row = 1
    rows_to_skip={}
    while skip_row<=limit_row:
        skip_row *= 7
        rows_to_skip[skip_row]=1
    step = 1
    base = step
    transition = 1
    inc = transition
    #ar = []
    idx = 0
    counter =1
    row = 0 
    total = 0
    while idx<=limit_row:
        #print(idx)
        for k in range(7):
            '''
            print('New batch: {0} to {1}. {2}'.format(idx,idx+6, base))
            if base==sequence[idx]:
                print('Success')
            else:
                print('Fail', base, sequence[row])
            '''
            row+=1
            for j in range(7):
                for i in range(1,8):
                    if idx in rows_to_skip:
                        idx += 1
                        total += 2
                        continue
                    if idx>limit_row:
                        return total
                    #ar.append(base*i)
                    total += base*i
                    idx += 1
                base += step
            step += inc
            base = step
            #print(ar)
            #ar = []
        inc += transition
        step = inc
        base = inc
        if inc>counter*7:
            transition += 1
            inc = transition
            step = inc
            base = inc
            counter += 1
        print(inc,transition)
# Wrong: 93294484786211968
# Wrong: 53311222694553802
# Wrong: 463239216834283032

if __name__ == "__main__":
    limit_row=int(2*10**4-1)
    print('The number of entries with numbers multiple of 7 in the pascal triangle in the first {0} rows is {1}'.format(limit_row+1,pascal_multiple_seven(limit_row)))#pascal_multiple_seven_alt(limit_row)))