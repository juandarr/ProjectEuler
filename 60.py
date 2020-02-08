"""
Finds the lowest sum of a set of five primes for which any two primes concatenate to produce another prime
Author: Juan Rios
"""

import math
from utils import prime_factors

lower_boundary = 26033
primes = prime_factors(lower_boundary)
primes_index = prime_factors(10**7, False)

"""
Returns 1 if the number is prime, 0 otherwise
"""
def is_prime(number):
    if number < len(primes_index):
        return primes_index[number]
    for p in primes:
        if p > math.sqrt(number):
            return 1
        if number%p==0:
            return 0

def reduce_candidates(candidates):
    pivot = candidates[0]
    tmp =[]
    for p in candidates[1:]:
        n1 = int(str(p)+str(pivot))
        n2 = int(str(pivot)+str(p))
        if is_prime(n1) and is_prime(n2):
            tmp.append(p)
    return tmp

"""
Returns the number lowest sum of set of five primes
"""
def lowest_prime_sum():
    min_sum = float('inf')
    for idx0 in range(2, len(primes)):
        prime_candidates0 = reduce_candidates(primes[idx0:])
        mod = primes[idx0]%3
        print(idx0)
        if primes[idx0]> lower_boundary/5:
            break
        for idx1 in range(len(prime_candidates0)):
            if prime_candidates0[idx1]%3 != mod:
                continue
            ar = [primes[idx0], prime_candidates0[idx1]]
            if sum(ar)>min_sum:
                break
            prime_candidates1 = reduce_candidates(prime_candidates0[idx1:])
            for idx2 in range(len(prime_candidates1)):
                if prime_candidates1[idx2]%3 != mod:
                    continue
                ar = [primes[idx0], prime_candidates0[idx1],prime_candidates1[idx2]]
                if sum(ar)>min_sum:
                    break
                prime_candidates2 =  reduce_candidates(prime_candidates1[idx2:])
                for idx3 in range(len(prime_candidates2)):
                    if prime_candidates2[idx3]%3 != mod:
                        continue
                    ar = [primes[idx0], prime_candidates0[idx1],prime_candidates1[idx2],prime_candidates2[idx3]]
                    if sum(ar)>min_sum:
                        break
                    prime_candidates3 =  reduce_candidates(prime_candidates2[idx3:])
                    for idx4 in range(len(prime_candidates3)):
                        if prime_candidates3[idx4]%3!=mod:
                            continue
                        ar = [primes[idx0], prime_candidates0[idx1],prime_candidates1[idx2],prime_candidates2[idx3],prime_candidates3[idx4]]
                        if min_sum > sum(ar):
                            min_sum = sum(ar)
                            print(ar, sum(ar))
                        else:
                            break
    return min_sum
                

    min_sum = float('inf')

    

            

        

if __name__ == "__main__":
    print('The lowest sum of a set of five primes is {0}'.format(lowest_prime_sum()))