"""
Finds the lowest sum of a set of five primes for which any two primes concatenate to produce another prime
Author: Juan Rios
"""

import math
from utils import prime_factors

"""
Returns 1 if the number is prime, 0 otherwise
"""
def is_prime(number, primes):
    for p in primes:
        if p > math.sqrt(number):
            return 1
        if number%p==0:
            return 0

"""
Returns the number lowest sum of set of five primes
"""
def lowest_prime_sum():
    #[3, 41, 719, 12413, 634679] 647855
    #[3, 349, 373, 1237, 240733] 242695
    primes = prime_factors(242695)
    primes_index = prime_factors(10**7, False)
    #remarkable_primes = [3,7,109,673]

    starting_index = 4
    completed = False
    max_sum = float('inf')

    while not(completed):
        index= starting_index
        remarkable_primes = [3,primes[index-1]]
        mod = remarkable_primes[1]%3
        while (len(remarkable_primes)<5):
        
            while (index < len(primes)):
                if (primes[index]%3!=mod):
                    index += 1
                    continue
                tmp = remarkable_primes + [primes[index]]
                all_prime = True
                for elem in tmp[:-1]:
                    n1 = int(str(elem)+str(tmp[-1]))
                    n2 = int(str(tmp[-1])+str(elem))
                    if n1<10**7 and n2<10**7:
                        if primes_index[n1]==0 or primes_index[n2]==0:
                            all_prime = False
                            break
                    else: 
                        if is_prime(n1, primes)==0 or is_prime(n2, primes)==0:
                            all_prime = False
                            break
                if all_prime:
                    remarkable_primes.append(primes[index])
                    #print(remarkable_primes)
                    index += 1
                    break
                index += 1
            if (index >= len(primes)):
                starting_index += 1
                break
        if (len(remarkable_primes)==5):
            if max_sum > sum(remarkable_primes):
                max_sum = sum(remarkable_primes)
                print(remarkable_primes, max_sum,index)
                starting_index += 1
                #completed = True
    return max_sum
        
if __name__ == "__main__":
    print('The lowest sum of a set of five primes is {0}'.format(lowest_prime_sum()))