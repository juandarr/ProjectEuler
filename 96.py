"""
Solves fifty sudoku puzzles and adds 3-digit values from the top left corner
Author: Juan Rios
"""
import math
import copy
from itertools import combinations

def read_sudoku(filename):
    """
    Read sudoku file
    """
    with open(filename) as sudoku_file:
        sudoku = sudoku_file.read()
    sudoku = sudoku.split('\n')
    puzzles = []
    for s in sudoku:
        if 'G' in s:
            puzzles.append([])
            continue
        puzzles[-1].append(s)
    return puzzles
    
def in_cluster(ar,cells,kind):
    in_row = True
    for idx in range(len(ar)-1):
        in_row &= ar[idx][0]==ar[idx+1][0]

    if kind==1:
        return in_row

    in_col = True
    for idx in range(len(ar)-1):
        in_col &= ar[idx][1]==ar[idx+1][1]

    if kind==2:
        return in_col

    in_group = False
    for cell in cells:
        row = True
        for idx in range(len(ar)):
            row &= ar[idx][0]>=(cell[0]-1)*3 and ar[idx][0]<(cell[0]*3)
        if row:
            col = True
            for idx in range(len(ar)):
                col &= ar[idx][1]>=(cell[1]-1)*3 and ar[idx][1]<(cell[1]*3)
            if col:
                in_group = True
                break
    if kind == 3:
        return in_group
    if kind ==0:
        return in_row or in_col or in_group

def which_group(opt,cells):
    group = 0
    for cell in cells:
        if opt[0]>=(cell[0]-1)*3 and opt[0]<(cell[0]*3) and opt[1]>=(cell[1]-1)*3 and opt[1]<(cell[1]*3):
            elem = (opt[0]-(cell[0]-1)*3)*3+(opt[1]-(cell[1]-1)*3)
            return elem,group
        group +=1 

def which_position(elem,group):
    row = (group//3)*3+elem//3 
    col = (group%3)*3+(elem%3)
    return (row,col)

def sudoku_solver(filename):
    puzzles = read_sudoku(filename)
    cells = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    #5(Done),6,41,47 
    total = 0
    for p_idx in range(0,len(puzzles)):
        puzzle = puzzles[p_idx]
        print(p_idx,puzzle)
        options = {}
        '''
        Check candidates for each unfilled position
        '''
        for cell in cells:
            candidates = set([i for i in range(1,10)])
            for r_idx in range((cell[0]-1)*3,cell[0]*3):
                for c_idx in range((cell[1]-1)*3,cell[1]*3):
                    if puzzle[r_idx][c_idx]!='0':
                        candidates.remove(int(puzzle[r_idx][c_idx]))

            for r_idx in range((cell[0]-1)*3,cell[0]*3):
                for c_idx in range((cell[1]-1)*3,cell[1]*3):
                    if puzzle[r_idx][c_idx]=='0':
                        tmp_candidates = copy.copy(candidates)
                        for number in puzzle[r_idx]:
                            tmp_candidates.discard(int(number))
                        for row in puzzle:
                            tmp_candidates.discard(int(row[c_idx]))
                        options[(r_idx,c_idx)]= tmp_candidates
        '''
            Look for unfilled positions with a unique candidate
        '''
        while sum([1 for opt in options if len(options[opt])==1])>0:
            to_remove = []
            for opt in options:
                if len(options[opt])==1:
                    tmp = list(options[opt])[0]
                    row = opt[0]
                    col = opt[1]
                    puzzle[row]=puzzle[row][:col]+str(tmp)+puzzle[row][col+1:]
                    to_remove.append([opt,tmp])
            for rem in to_remove:
                options.pop(rem[0])
                for opt in options:
                    if in_cluster([rem[0],opt],cells,0):
                        if rem[1] in options[opt]:
                            options[opt].remove(rem[1])

        c = 0
        solved = False

        while not(solved):
            solved = True
            
            '''
            Check for length of union of sets in x positions equal to x in rows
            '''
            
            rows=[]
            to_remove = []
            for opt in options:
                if len(rows)>opt[0]:
                    rows[opt[0]].append(opt[1])
                else:
                    while len(rows)<=opt[0]:
                        rows.append([])
                    rows[opt[0]].append(opt[1])
            for row in range(len(rows)):
                for r in range(2,len(rows[row])):
                    for comb in combinations(rows[row],r):
                        tmp = set()
                        for idx in comb:
                            tmp = tmp.union(options[(row,idx)])
                        if r==len(tmp):
                            to_remove.append([row,comb,list(tmp)])
            #print(to_remove)
            for rem in to_remove:
                for opt in options:
                    if opt[0]==rem[0] and opt not in [(opt[0],i) for i in rem[1]]:
                        for disc in rem[2]:
                            options[opt].discard(disc)
            
            '''
            Look for unfilled positions with a unique candidate
            '''
            while sum([1 for opt in options if len(options[opt])==1])>0:
                to_remove = []
                for opt in options:
                    if len(options[opt])==1:
                        tmp = list(options[opt])[0]
                        row = opt[0]
                        col = opt[1]
                        puzzle[row]=puzzle[row][:col]+str(tmp)+puzzle[row][col+1:]
                        to_remove.append([opt,tmp])
                for rem in to_remove:
                    options.pop(rem[0])
                    for opt in options:
                        if in_cluster([rem[0],opt],cells,0):
                            if rem[1] in options[opt]:
                                options[opt].remove(rem[1])

            '''
            Check for length of union of sets in x positions equal to x in columns
            '''
            
            cols=[]
            to_remove = []
            for opt in options:
                if len(cols)>opt[1]:
                    cols[opt[1]].append(opt[0])
                else:
                    while len(cols)<=opt[1]:
                        cols.append([])
                    cols[opt[1]].append(opt[0])
            for col in range(len(cols)):
                for r in range(2,len(cols[col])):
                    for comb in combinations(cols[col],r):
                        tmp = set()
                        for idx in comb:
                            tmp = tmp.union(options[(idx,col)])
                        if r==len(tmp):
                            to_remove.append([col,comb,list(tmp)])
            #print(to_remove)
            for rem in to_remove:
                for opt in options:
                    if opt[1]==rem[0] and opt not in [(i,opt[1]) for i in rem[1]]:
                        for disc in rem[2]:
                            options[opt].discard(disc)
            
            '''
            Look for unfilled positions with a unique candidate
            '''
            while sum([1 for opt in options if len(options[opt])==1])>0:
                to_remove = []
                for opt in options:
                    if len(options[opt])==1:
                        tmp = list(options[opt])[0]
                        row = opt[0]
                        col = opt[1]
                        puzzle[row]=puzzle[row][:col]+str(tmp)+puzzle[row][col+1:]
                        to_remove.append([opt,tmp])
                for rem in to_remove:
                    options.pop(rem[0])
                    for opt in options:
                        if in_cluster([rem[0],opt],cells,0):
                            if rem[1] in options[opt]:
                                options[opt].remove(rem[1])
            '''
            Check for length of union of sets in x positions equal to x in groups
            '''
            groups=[]
            to_remove = []
            for opt in options:
                elem,g = which_group(opt,cells)
                if len(groups)>g:
                    groups[g].append(elem)
                else:
                    while len(groups)<=g:
                        groups.append([])
                    groups[g].append(elem)
            for group in range(len(groups)):
                for r in range(2,len(groups[group])):
                    for comb in combinations(groups[group],r):
                        tmp = set()
                        for idx in comb:
                            pos = which_position(idx,group)
                            #print(idx,group,pos)
                            tmp = tmp.union(options[pos])
                        if r==len(tmp):
                            to_remove.append([group,comb,list(tmp)])
            #print(to_remove)
            for rem in to_remove:
                for opt in options:
                    elem,g = which_group(opt,cells)
                    if g==rem[0] and opt not in [which_position(i,rem[0]) for i in rem[1]]:
                        for disc in rem[2]:
                            options[opt].discard(disc)
            
            '''
            Look for unfilled positions with a unique candidate
            '''
            while sum([1 for opt in options if len(options[opt])==1])>0:
                to_remove = []
                for opt in options:
                    if len(options[opt])==1:
                        tmp = list(options[opt])[0]
                        row = opt[0]
                        col = opt[1]
                        puzzle[row]=puzzle[row][:col]+str(tmp)+puzzle[row][col+1:]
                        to_remove.append([opt,tmp])
                for rem in to_remove:
                    options.pop(rem[0])
                    for opt in options:
                        if in_cluster([rem[0],opt],cells,0):
                            if rem[1] in options[opt]:
                                options[opt].remove(rem[1])

            if len(options):
                solved = False
            c +=1
            if c<20:
                print(puzzle)
            if c==10:
                for s in options:
                    if len(options[s]):
                        print(s,options[s])
        puzzles[p_idx] = puzzle
        print('Solution: {0}'.format(puzzle))
        total += int(puzzle[0][:3])
    return total

if __name__ == "__main__":
    #filename = 'files/sudoku.txt'
    filename = 'files/sudoku_test.txt'
    cells = [[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    print('The sum of all 3-digit number of all solutions is {0}'.format(sudoku_solver(filename))) 
  