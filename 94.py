"""
Finds the sum of the perimeters of all almost equilaterals with p below or equal to 10**9
Author: Juan Rios
"""
import math

def almost_equilateral(limit_exp):
    p = 0
    for a in range(3,(limit_exp-1)//3+1,2):
        s_a = [a*(3*a-2)-1,a*(3*a+2)-1]
        b_a = [math.sqrt(s_a[0]), math.sqrt(s_a[1])]
        inc = [1,-1]
        for b_idx in range(len(b_a)): 
            if int(b_a[b_idx]+0.5)**2==s_a[b_idx]:
                b = int(b_a[b_idx]+0.5)
                if b%4==0 or (a+inc[b_idx])%4==0:
                    p += 3*a+inc[b_idx]
                elif b%2==0 and (a+inc[b_idx])%2==0:
                    p += 3*a+inc[b_idx]
    return p
        
if __name__ == "__main__":
    limit_exp = 10**9
    print('The sum of perimeters of all almost equilaterals with perimeters below or equal to {0} is {1}'.format(limit_exp, almost_equilateral(limit_exp))) 

