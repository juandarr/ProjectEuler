"""
Finds sum of all values in the diagonals of a clockwise spiral of integers starting with one at the center
Author: Juan Rios
"""

def spiral_diagonal_sum(dimension):
    total = 1+3+5+7+9
    sum_n = 0
    for i in range(5,dimension+1,2):
        total += i**2
        sum_n += (i-3)//2
        for inc in (2,4,6):
            total += 1+(inc*(i-1)//2)+(8*sum_n)
    return total
if __name__ == "__main__":
    dimension = 1001
    print('The sum of all values in the diagonal of the {0}x{0} spiral is {1}'.format(dimension,spiral_diagonal_sum(dimension)))