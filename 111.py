"""
Finds sum of all runs of primes with maximum 1-9 digits repetitions
Author: Juan Rios
"""
import math
from utils import prime_factors
def is_prime(num, primes):
    '''
    returns primes that are above below_limit and below above_limit
    '''
    for p in primes:
        if p >int(math.sqrt(num)):
            return True
        elif num%p==0:
            return False

def max_checker(num,m,n,s):
    freq = {}
    sorted_num = sorted(num)
    prev_idx = 0
    for idx in range(1,len(sorted_num)):
        if sorted_num[idx]!=sorted_num[idx-1]:
            freq[sorted_num[idx-1]] = idx-prev_idx
            prev_idx = idx
    freq[sorted_num[-1]]=len(sorted_num)-prev_idx
    for d in freq:
        if freq[d]>m[d]:
            m[d]=freq[d]
            n[d]=1
            s[d]= int(num)
        elif freq[d]==m[d]:
            n[d] += 1
            s[d] += int(num)

def primes_runs():
    primes = prime_factors(100005)
    m = {}
    n = {}
    s = {}
    multiple = 9
    limit = int('9'*multiple)
    digits= '0123456789'
    for d in digits:
        m[d]=0
        n[d]=0
        s[d]=0

    visited = {}
    for d1 in digits:
        ar = d1*multiple
        for d2 in digits:
            if d2!=d1:
                for idx in range(len(n)+1):
                    num = ar[:idx]+d2+ar[idx:]
                    num_int =int(num)
                    if num_int>limit:
                        if num not in visited:
                            visited[num]=1
                            if is_prime(num_int,primes):
                                max_checker(num,m,n,s)
    complement = ''.join([d for d in digits if m[d]!=multiple])
    for d1 in complement:
        ar = d1*(multiple-1)
        for d2 in ''.join([d for d in digits if d!=d1]):
            for idx in range(len(ar)+1):
                num = ar[:idx]+d2+ar[idx:]
                for d3 in ''.join([d for d in digits if d!=d1]):
                    for idx1 in range(len(num)+1):
                        num1 = num[:idx1]+d3+num[idx1:]
                        num1_int = int(num1)
                        if num1_int>limit:
                            if num1 not in visited:
                                visited[num1]=1
                                if is_prime(num1_int,primes):
                                    max_checker(num1,m,n,s)
    return sum(s.values())

if __name__ == "__main__":
    print('The sum of all runs of primes with maximum 1-9 digits repetitions is {0}'.format(primes_runs())) 