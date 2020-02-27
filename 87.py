"""
Finds the amount of number below 50 million for the formula a**2+b**3+c**4, where a,b,c are primes
Author: Juan Rios
"""
import math
from utils import prime_factors

"""
Generates combinations of number according to the triple prime formula, here b>a
"""
def triplet_generation(a,b,limit_value):
    pot = [i for i in [b**2+a**3+a**4,a**2+b**3+a**4,a**2+a**3+b**4,b**2+b**3+a**4,b**2+a**3+b**4,a**2+b**3+b**4] if i<limit_value]
    return pot

"""
Calculates the amount of values from primes and formula
"""
def prime_triplets(limit_value):
    primes = prime_factors(int(math.sqrt(limit_value))+1)
    total = 0
    values = []

    for pivot in range(len(primes)):
        for index in range(pivot):
            if (primes[pivot]**2+primes[index]**3+primes[index]**4)>=limit_value:
                break
            triplet_variation = triplet_generation(primes[index], primes[pivot], limit_value)
            total += len(triplet_variation)
            values += triplet_variation
        pivot_triplet = primes[pivot]**2+primes[pivot]**3+primes[pivot]**4
        if pivot_triplet<limit_value:
            total += 1
            values.append(pivot_triplet)
    return len(set(values))

"""
Calculates the amount of values from primes and formula
"""
def prime_triplets_bf(limit_value):
    primes = prime_factors(int(math.sqrt(limit_value))+1)
    total = 0
    values = []

    for a in range(len(primes)):
        for b in range(len(primes)):
            pt1 = primes[a]**2+primes[b]**3
            if pt1>=limit_value:
                break
            for c in range(len(primes)):
                pt2 = pt1+primes[c]**4
                if pt2>=limit_value:
                    break
                total += 1
                values.append(pt2)
    return len(set(values))

if __name__ == "__main__":
    limit_value = 50*(10**6)
    print('The amount of numbers below {0} from prime triplets is {1}'.format(limit_value,prime_triplets_bf(limit_value)))