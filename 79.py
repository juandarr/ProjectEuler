"""
Finds the passcode given a list of potential code positions
Author: Juan Rios
"""
import math
import numpy as np

codes = """319
680
180
690
129
620
762
689
762
318
368
710
720
710
629
168
160
689
716
731
736
729
316
729
729
710
769
290
719
680
318
389
162
289
162
718
729
319
790
680
890
362
319
760
316
729
380
319
728
716"""

codes = codes.split('\n')

"""
Calculate the possible number of partitions
"""
def passcode(codes):
    before = {}
    after = {}
    for code in codes:
        for i in range(2):
            if code[i] not in after:
                after[code[i]] = set(code[i+1])
                if len(code[i+1:3])>1:
                    after[code[i]].add(code[i+2])
            else:
                for e in code[i+1:3]:
                    after[code[i]].add(e)

            if code[2-i] not in before:
                before[code[2-i]] = set(code[0])
                if len(code[:2-i])>1:
                    before[code[2-i]].add(code[1])
            else:
                for e in code[:2-i]:
                    before[code[2-i]].add(e)
    return compress_info(before,after)


       

def compress_info(ar_before,ar_after):
    length = 0 
    tmp = []
    for h in range(10):
        for c in range(10):
            ch = str(c)
            if length == 0:
                if ch not in ar_before and ch not in ar_after:
                    continue
                elif ch not in ar_before:
                    tmp.append(ch)
                    break
            else:
                if ch in ar_before:
                    if length == len(ar_before[ch]):
                        if set(tmp)-ar_before[ch]==set():
                            tmp.append(ch)
                            break
        length += 1
    return int(''.join(tmp))

if __name__ == "__main__":
    print('The passcode given the code position is {0}'.format(passcode(codes))) 