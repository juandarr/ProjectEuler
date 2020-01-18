"""
Finds the largest path from top to botton un a pyramid of numbers
Author: Juan Rios
"""
import math

values = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

values = values.split("\n")
for i in range(len(values)):
    values[i] = values[i].split(' ')

"""
returns the largest path from top to bottom in a pyramid of numbers
Using greedy Dijkstra algorithm
"""
def greedy_largest_path(values):
    starting_node = [0,0,int(values[0][0])]
    unvisited = [starting_node]
    stored_vals = []
    visited = []
    for i in range(len(values)):
        stored_vals.append([0]*(i+1))
        visited.append([0]*(i+1))
    stored_vals[0][0] = starting_node[2]
    while (unvisited):
        current_node = unvisited.pop()
        i = current_node[0]
        j = current_node[1]
        visited[i][j] = 1
        tmp = []
        for c in range(2):
            if (stored_vals[i+1][j+c] < stored_vals[i][j] + int(values[i+1][j+c])):
                stored_vals[i+1][j+c] = stored_vals[i][j] + int(values[i+1][j+c])
                if (i+1)!=len(values)-1:
                    if visited[i+1][j+c]==0:
                        unvisited.append([i+1, j+c, stored_vals[i+1][j+c]])
        unvisited.sort(key = lambda a: a[2])
    return max(stored_vals[-1])

"""
returns the largest path from top to bottom in a pyramid of numbers
Using dynamic programming 
"""
def dp_largest_path(values):
    for i in range(len(values)-1,0,-1):
        for j in range(0,len(values[i])-1):
            values[i-1][j] = int(values[i-1][j])+ max(int(values[i][j]), int(values[i][j+1]))
    return values[0][0]
    
if __name__ == "__main__":
    print('The largest sum of values of numbers from top to botton is {0}'.format(dp_largest_path(values)))
