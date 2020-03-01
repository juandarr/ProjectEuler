"""
Finds the number of arrangements of two dices than can generate the squares from 1 to 9
Author: Juan Rios
"""
import math
from itertools import combinations

def check_arrangement(d1, d2):
    """
    Check if arrangements follow the rules
    """
    rules = [[[1,4,9],[1,4,6]],[[0,6,8],[0,9,8]],[[5]],[[6],[9]],[[6],[9]],[[2]],[[0,1,3,4]],[None],[[1]]]
    rule_followed = True
    rule_index = 0
    while rule_followed and rule_index<len(rules):
        if rules[rule_index][0]!=None and rule_index!=6:
            rule_followed = False
            for rule in rules[rule_index]:
                values = []
                if rule_index in d1:
                    for v in list(d2):
                        if v in rule:
                            values.append(v)
                if rule_index in d2:
                    for v in list(d1):
                        if v in rule:
                            values.append(v)
                if values!=[]:
                    if set(values)==set(rule):
                        rule_followed = True
                        break
        elif rules[rule_index][0]!=None and rule_index==6: 
            rule_followed = False
            for rule in rules[rule_index]:
                values = []
                if rule_index in d1 or 9 in d1:
                    for v in list(d2):
                        if v in rule:
                            values.append(v)
                if rule_index in d2 or 9 in d2:
                    for v in list(d1):
                        if v in rule:
                            values.append(v)
                if values!=[]:
                    if set(values)==set(rule):
                        rule_followed = True
                        break
        else:
            rule_followed = True
        rule_index += 1
        
    return rule_followed
    


def number_of_arrangements(squares):
    """
    Calculates the number of arrangements of two dices
    """
    arrangements = {}
    for dice1 in combinations([i for i in range(10)],6):
        d1 = set(dice1)
        for dice2 in combinations([i for i in range(10)],6):
            d2 = set(dice2)
            if check_arrangement(d1,d2):      
                if (dice1,dice2) not in arrangements:
                    if (dice2,dice1) not in arrangements:
                        arrangements[(dice1,dice2)]=1
    return len(arrangements)

if __name__ == "__main__":
    squares = [i**2 for i in range(1,10)]
    print('The number of arrangements of 2 dices to generate the squares is {0}'.format(number_of_arrangements(squares))) 