"""
Finds the largest square formed by any member of a set of anagram pairs
Author: Juan Rios
"""
import math
from itertools import permutations

def read_words(filename):
    """
    Read words file
    """
    with open(filename) as words_file:
        words = words_file.read()
    words = words.split('","')
    words[0]=words[0][1:]
    words[-1]=words[-1][:-1]
    return words

def group_pairs(filename):
    words = read_words(filename)
    print('Putting words together in groups')
    words = sorted(words,key=len, reverse=True)
    groups = {}
    visited = {}
    for idx in range(len(words)):
        if words[idx] not in visited:
            letters_sorted = sorted(words[idx])
            visited[words[idx]]=letters_sorted
        else:
            letters_sorted = visited[words[idx]]
        for idx_p in range(idx+1,len(words)):
            if words[idx_p] not in visited:
                letters_sorted_p = sorted(words[idx_p])
                visited[words[idx_p]]=letters_sorted_p
            else:
                letters_sorted_p = visited[words[idx_p]]
            if letters_sorted==letters_sorted_p and words[idx]!=words[idx_p][-1::-1]:
                union = set(letters_sorted)
                g = len(union)
                union_list= []
                if g <=10:
                    together = words[idx]
                    for i in together:
                        if i in union:
                            union_list.append(i)
                            union.discard(i)
                    if g in groups:
                        groups[g].append([words[idx],words[idx_p],union_list])
                    else:
                        groups[g] = [[words[idx],words[idx_p],union_list]]
    for g in groups:
        groups[g]=sorted(groups[g], key=lambda x: len(x[0]), reverse=True)
    return groups

def check_squares_permutations(filename):
    groups = group_pairs(filename)
    i = 1
    squares = {}
    print('Calculating squares')
    while (i**2<10**10):
        squares[i**2]=i
        i+=1
    largest = 0
    largest_str = str(largest)
    print('Testing combinations')
    for g in groups:
        permut = list(permutations([0,1,2,3,4,5,6,7,8,9],g))
        for per in permut[-1::-1]:
            for pair in groups[g]:
                if len(pair[0])<len(largest_str):
                    continue
                code = {}
                for idx in range(len(pair[2])):
                    code[pair[2][idx]]=per[idx]
                values = []
                anagram = True
                for word in pair[:2]:
                    num = ''
                    for letter in word:
                        num += str(code[letter])
                    if num[0]=='0':
                        anagram = False
                        break
                    num = int(num)
                    if num in squares:
                        values.append(num)
                    else:
                        anagram = False
                        break
                if anagram:
                    if largest<max(values):
                        largest = max(values)
                        largest_str = str(largest)
                    print(pair,largest)
                        
    return largest

if __name__ == "__main__":
    filename = 'files/words.txt'
    print('The the largest square formed by any member of a set of anagram pairs is {0}'.format(check_squares_permutations(filename))) 