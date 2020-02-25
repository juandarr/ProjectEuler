"""
Finds the odds in the monopoly game for two 4 sided dices
Author: Juan Rios
"""
import math
import numpy as np
import random 
#random.seed(a=4)

class rules_deck():
    def __init__(self):
        self.cc = [0,10]
        random.shuffle(self.cc)
        self.ch = [0,10,11,24,39,5]
        random.shuffle(self.ch)
        self.cc_counter = 0
        self.ch_counter = 0

    def apply_rule_and_move(self, current_cell):
        next_cell = current_cell

        if next_cell in [7,22,36]:
            self.ch_counter %= 16
            if self.ch_counter<len(self.ch):
                next_cell = self.ch[self.ch_counter]
            elif self.ch_counter in [6,7]:
                if current_cell==7:
                    next_r = 15
                elif current_cell==22:
                    next_r = 25
                elif current_cell==36:
                    next_r = 5
                next_cell = next_r
            elif self.ch_counter==8:
                if current_cell==7:
                    next_u = 12 
                elif current_cell==22:
                    next_u = 28
                elif current_cell==36:
                    next_u = 12
                next_cell = next_u
            elif self.ch_counter==9:
                next_cell = current_cell-3
            else:
                next_cell = current_cell
            self.ch_counter += 1

        if next_cell in [2,17,33]:
            self.cc_counter %= 16
            if self.cc_counter<len(self.cc):
                next_cell = self.cc[self.cc_counter]
            else:
                next_cell = current_cell
            self.cc_counter +=1
            
        
        if next_cell==30:
            next_cell = 10
        return next_cell

class monopoly_game():

    def __init__(self,dice_sides):
        self.doubles = 0
        self.previous_double = False
        self.sides = dice_sides
        self.rules = rules_deck()
        self.outcomes = {}
        for i in range(40):
            self.outcomes[i]=0

    def roll_dices(self):
        dice1 = random.randint(1,self.sides)
        dice2 = random.randint(1,self.sides)
        if dice1==dice2 and self.doubles == 0:
            self.doubles = 1
            self.previous_double = True
        elif dice1==dice2 and self.previous_double:
            self.doubles += 1
        else:
            self.doubles = 0
            self.previous_double = False
        return dice1+dice2

    def one_step_game(self,current_position):
        dice_move = self.roll_dices()
        if self.doubles==3:
            self.doubles = 0
            self.previous_double = False
            next_position = 10
            self.outcomes[next_position]+=1
        else:
            next_position = self.rules.apply_rule_and_move(dice_move+current_position)%40
            self.outcomes[next_position]+=1
        return next_position

if __name__ == "__main__":
    sides = 4
    monopoly = monopoly_game(sides)
    position = 0
    for _ in range(10**6):
        position = monopoly.one_step_game(position)
    total = sum([i[1] for i in sorted(monopoly.outcomes.items() ,  key=lambda x: x[1], reverse=True)])
    for key in monopoly.outcomes:
        monopoly.outcomes[key] /= total
    sol=sorted(monopoly.outcomes.items() ,  key=lambda x: x[1], reverse=True)
    print('The odds of a number given two {0} sided dices is {1}'.format(sides,[i[0] for i in sol[:3] ]))