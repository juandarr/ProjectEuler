"""
Finds the number of chains with numbers starting below one million with 60 non-repeating terms
Author: Juan Rios
"""

import math

def chains_counter(limit_value):
    factorials = [math.factorial(i) for i in range(10)]
    counter = 0
    visited = {}
    for i in range(1,limit_value+1):
        if i not in visited:
            seq_index = {i:1}
            seq = [i]
            number = sum([factorials[int(s)] for s in str(i)])
            if number in visited:
                if 1+visited[number]==60:
                    counter += 1
                visited[i] = 1+visited[number]
                continue
            check_sequence = True
            while True:
                if number in seq_index:
                    if len(seq)==60:
                        counter += 1
                    rep = number
                    break
                else:
                    seq_index[number] = 1
                    seq.append(number)
                number = sum([factorials[int(s)] for s in str(number)])
                if number in visited:
                    if len(seq)+visited[number]==60:
                        counter += 1
                    check_sequence = False
                    rep = number
                    break
            if check_sequence:
                index_rep = seq.index(rep)
                for index in range(len(seq)):    
                    if seq[index] not in visited:
                        if index<index_rep:
                            visited[seq[index]]=len(seq)-index
                        else:
                            visited[seq[index]]=len(seq)-index_rep
            else:
                for index in range(len(seq)):    
                    if seq[index] not in visited:
                        visited[seq[index]]=len(seq)-index+visited[rep]
    return counter


if __name__ == "__main__":
    limit_value = 10**6
    print('The number of chains with 60 non-repeating terms is {0}'.format(chains_counter(limit_value)))