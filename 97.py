"""
Finds last 10 digits of the a non-Mersenne prime
Author: Juan Rios
"""
import math

def product(limit_exp,exp,mul):
    
    digits = [0]*10
    i = 1
    digits[9]=1
    while i<=limit_exp:
        quot = 0
        for d in range(len(digits)-1,-1,-1):
            num = digits[d]*exp + quot
            quot = num//10
            res = num%10
            digits[d]=res
        i += 1
    val = int(''.join([str(i) for i in digits]))
    print(val)
    mult = str(mul)
    solution  = 0
    for i in range(len(mult)-1,-1,-1):
        solution += val*int(mult[i])*(10**(len(mult)-i-1))
    return str(solution)[-10:]
        
if __name__ == "__main__":
    limit_exp = 7830457
    print('The last 10 digits of the non-Mersenne prime are {0}'.format(product(limit_exp,2,28433))) 