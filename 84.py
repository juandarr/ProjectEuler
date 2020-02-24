"""
Finds the odds in the monopoly game for two 4 sided dices
Author: Juan Rios
"""
import math

"""
Calculates the number of rectangles in a l*h grid
"""
def dices(sides):
    dice_odds = {}
    for i in range(1,sides+1):
        for j in range(1,sides+1):
            if i+j in dice_odds:
                dice_odds[i+j]+= 1
            else:
                dice_odds[i+j] = 1
    return dice_odds

def monopoly_rules(current_cell,remove= False, elements_to_remove=[]):
    if remove==False:
        total = 16
    else:
        total = 16 - len(elements_to_remove)

    if current_cell in [2,17,33]:
        ar = [[1/total,10],[1/total,0],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell]]
        if remove==False:
            return ar
        else:
            tmp = []
            for i in range(len(ar)):
                if i not in elements_to_remove:
                    tmp.append(ar[i])
            return tmp
    elif current_cell in [7,22,36]:
        if current_cell==7:
            next_u = 12 
            next_r = 15
        elif current_cell==22:
            next_u = 28
            next_r = 25
        elif current_cell==36:
            next_u = 12
            next_r = 5
        ar = [[1/total,0],[1/total,10],[1/total,11],[1/total,24],[1/total,39],[1/total,5],[1/total,next_r],[1/total,next_r],[1/total,next_u],[1/total,current_cell-3],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell],[1/total,current_cell]]
        if remove==False:
            return ar
        else:
            tmp = []
            for i in range(len(ar)):
                if i not in elements_to_remove:
                    tmp.append(ar[i])
            return tmp
    elif current_cell==30:
        return [[None,10]]
    else:
        return [[None,current_cell]]

def monopoly_cell_odds(sides):
    monopoly_odds = {}
    dice_odds = dices(sides)
    total = sides*sides
    for key in dice_odds:
        current_cell = 0
        current_cell += key
        options = monopoly_rules(current_cell)
        if key%2==1:
            for opt in options:
                prob = dice_odds[key]/total
                if opt[0]==None:
                    if opt[1] in monopoly_odds:
                        monopoly_odds[opt[1]] += prob
                    else:
                        monopoly_odds[opt[1]] = prob
                else:
                    if opt[1] in monopoly_odds:
                        monopoly_odds[opt[1]] += prob*opt[0]
                    else:
                        monopoly_odds[opt[1]] = prob*opt[0]
        else:
            prob = (dice_odds[key]-1)/total
            for opt in options:
                index0 = options.index(opt)
                if opt[0]==None:
                    if opt[1] in monopoly_odds:
                        monopoly_odds[opt[1]] += prob
                    else:
                        monopoly_odds[opt[1]] = prob
                else:
                    if opt[1] in monopoly_odds:
                        monopoly_odds[opt[1]] += prob*opt[0]
                    else:
                        monopoly_odds[opt[1]] = prob*opt[0]
                for key in dice_odds:
                    tmp_cell = opt[1]
                    tmp_cell += key
                    tmp_cell %=40
                    if current_cell in [7,22,36] and tmp_cell in [7,22,36]:
                        tmp_options = monopoly_rules(tmp_cell, True, [index0])
                    elif current_cell in [2,17,33] and tmp_cell in [2,17,33]:
                        tmp_options = monopoly_rules(tmp_cell, True, [index0])
                    else:
                        tmp_options = monopoly_rules(tmp_cell)
                    if key%2==1:
                        for tmp_opt in tmp_options:
                            tmp_prob = (1/total)*(dice_odds[key]/total)
                            if tmp_opt[0]==None:
                                if tmp_opt[1] in monopoly_odds:
                                    monopoly_odds[tmp_opt[1]] += tmp_prob
                                else:
                                    monopoly_odds[tmp_opt[1]] = tmp_prob
                            else:
                                if tmp_opt[1] in monopoly_odds:
                                    monopoly_odds[tmp_opt[1]] += tmp_prob*tmp_opt[0]
                                else:
                                    monopoly_odds[tmp_opt[1]] = tmp_prob*tmp_opt[0]
                    else:
                        for tmp_opt in tmp_options:
                            index1 = tmp_options.index(tmp_opt)
                            tmp_prob = (1/total)*((dice_odds[key]-1)/total)
                            if tmp_opt[0]==None:
                                if tmp_opt[1] in monopoly_odds:
                                    monopoly_odds[tmp_opt[1]] += tmp_prob
                                else:
                                    monopoly_odds[tmp_opt[1]] = tmp_prob
                            else:
                                if tmp_opt[1] in monopoly_odds:
                                    monopoly_odds[tmp_opt[1]] += tmp_prob*tmp_opt[0]
                                else:
                                    monopoly_odds[tmp_opt[1]] = tmp_prob*tmp_opt[0]
                            for key in dice_odds:
                                tmp2_cell = tmp_opt[1]
                                tmp2_cell += key
                                tmp2_cell %=40
                                if tmp_cell in [7,22,36] and tmp2_cell in [7,22,36]:
                                    tmp_index = index1
                                    if index1 >= index0:
                                        tmp_index = index1+1
                                    tmp2_options = monopoly_rules(tmp2_cell, True, [index0,tmp_index])
                                elif tmp_cell in [2,17,33] and tmp2_cell in [2,17,33]:
                                    tmp_index = index1
                                    if index1 >= index0:
                                        tmp_index = index1+1
                                    tmp2_options = monopoly_rules(tmp2_cell, True, [index0,tmp_index])
                                else:
                                    tmp2_options = monopoly_rules(tmp2_cell)
                                if key%2==1:
                                    for tmp2_opt in tmp2_options:
                                        tmp2_prob = ((1/total)**2)*(dice_odds[key]/total)
                                        if tmp2_opt[0]==None:
                                            if tmp2_opt[1] in monopoly_odds:
                                                monopoly_odds[tmp2_opt[1]] += tmp2_prob
                                            else:
                                                monopoly_odds[tmp2_opt[1]] = tmp2_prob
                                        else:
                                            if tmp2_opt[1] in monopoly_odds:
                                                monopoly_odds[tmp2_opt[1]] += tmp2_prob*tmp2_opt[0]
                                            else:
                                                monopoly_odds[tmp2_opt[1]] = tmp2_prob*tmp2_opt[0]
                                else:
                                    tmp2_prob = ((1/total)**2)*((dice_odds[key]-1)/total)
                                    for tmp2_opt in tmp2_options:
                                        if tmp2_opt[0]==None:
                                            if tmp2_opt[1] in monopoly_odds:
                                                monopoly_odds[tmp2_opt[1]] += tmp2_prob
                                            else:
                                                monopoly_odds[tmp2_opt[1]] = tmp2_prob
                                        else:
                                            if tmp2_opt[1] in monopoly_odds:
                                                monopoly_odds[tmp2_opt[1]] += tmp2_prob*tmp2_opt[0]
                                            else:
                                                monopoly_odds[tmp2_opt[1]] = tmp2_prob*tmp2_opt[0]
                                        prob_jail =((1/total)**3)
                                        if 10 in monopoly_odds:
                                            monopoly_odds[10]+= prob_jail
                                        else:
                                            monopoly_odds[10] = prob_jail
    return sorted(monopoly_odds.items() ,  key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    sides = 6 
    print('The odds of a number given two {0} sided dices is {1}'.format(sides,monopoly_cell_odds(sides)))