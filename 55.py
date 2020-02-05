"""
Finds the number of lychrel numbers below ten thousand
Author: Juan Rios
"""

import math

"""
Return number of lychrel numbers below ten thousand
"""
def lychrel_counter(limit_value):
    number = 10
    visited = [0]*10**6
    lychrel_counter = 0
    while number < limit_value:
        if not(visited[number]):
            last_visited = []
            is_lychrel = True
            tmp_number = number
            for i in range(49):
                reverse = int(str(tmp_number)[::-1])
                tmp_number += reverse
                last_visited += [reverse, tmp_number]
                if str(tmp_number)==str(tmp_number)[::-1]:
                    is_lychrel = False
                    break
                if tmp_number<10**6:
                    if visited[tmp_number]:
                        is_lychrel = False
                        break
            if is_lychrel:
                lychrel_counter += 1
            else:
                for num in last_visited[:-1]:
                     if num<10**6:
                        visited[num] = 1
        number += 1
    return lychrel_counter


if __name__ == "__main__":
    limit_value = 10**4
    print('The number of lychrel numbers below {0} is {1}'.format(limit_value, lychrel_counter(limit_value)))