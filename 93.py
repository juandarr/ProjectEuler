"""
Finds the combination of digits with the longest set of consecutive positive integers
Author: Juan Rios
"""
import math
from itertools import combinations,permutations,combinations_with_replacement

def expression_generation():
    operators = ['+','-','*','/']
    max_sequence = 0
    max_set = ()
    for set_values in combinations([i for i in range(1,10)],4):
        values = set()
        for perm in permutations(set_values):
            for op_comb in combinations_with_replacement([i for i in range(4)],3):
                for op in permutations(op_comb):
                    exp = []

                    exp.append('{7}{7}{0}{1}{2}{8}{3}{4}{8}{5}{6}'.format(perm[0],operators[op[0]],perm[1],operators[op[1]],perm[2],operators[op[2]],perm[3],'(',')'))
                    exp.append('{7}{0}{1}{2}{8}{3}{7}{4}{5}{6}{8}'.format(perm[0],operators[op[0]],perm[1],operators[op[1]],perm[2],operators[op[2]],perm[3],'(',')'))
                    exp.append('{7}{0}{1}{7}{2}{3}{4}{8}{8}{5}{6}'.format(perm[0],operators[op[0]],perm[1],operators[op[1]],perm[2],operators[op[2]],perm[3],'(',')'))
                    exp.append('{0}{1}{7}{7}{2}{3}{4}{8}{5}{6}{8}'.format(perm[0],operators[op[0]],perm[1],operators[op[1]],perm[2],operators[op[2]],perm[3],'(',')'))
                    exp.append('{0}{1}{7}{2}{3}{7}{4}{5}{6}{8}{8}'.format(perm[0],operators[op[0]],perm[1],operators[op[1]],perm[2],operators[op[2]],perm[3],'(',')'))

                    for e in exp:
                        try:
                            number = eval(e)
                            if number==int(number) and number>0:
                                values.add(int(number))
                        except:
                            continue
        values = sorted(list(values))
        chains = [1]
        counter = 1
        for i in range(len(values)-1):
            if values[i+1]-values[i]==1:
                counter += 1
            else:
                chains.append(counter)
                if len(values[i:])<max(chains):
                    break
                counter = 1
            i += 1

        sequence = max(chains)
        if sequence > max_sequence:
            max_sequence = sequence
            max_set = set_values
    return ''.join([str(i) for i in max_set])
                

if __name__ == "__main__":
    print('The combination generation the largest chain of consecutive positive integers is {0}'.format(expression_generation())) 