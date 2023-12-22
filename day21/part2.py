import numpy as np
from collections import deque
from math import ceil

DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

file = open("day21/input.txt")
plot = [l.strip()*5 for l in file.readlines()]*5
rows = int(len(plot) / 5)
cols = int(len(plot[0]) / 5)

current_s = 0
starting_point = None
for i in range(rows*2, rows*3):
    s_index = plot[i].find("S", cols*2, cols*3)
    if s_index != -1:
        starting_point = (i, s_index)
        break


STEPS = 26501365
STEP_REM = STEPS % rows

def get_reachable(end_distance):
    end_mod = end_distance % 2
    
    visited = {}
    q = deque([(starting_point, 0)])
    while q:
        point, distance = q.popleft()
        
        for d in DIRECTIONS:
            next_point = (point[0] + d[0], point[1] + d[1])
            if plot[next_point[0]][next_point[1]] != "#": #next_point[0] >= 0 and next_point[1] >= 0 and next_point[0] < (rows*3) and next_point[1] < (cols*3) and 
                next_distance = distance + 1
                    
                
                if next_point not in visited:
                    visited[next_point] = next_distance
                    if next_distance < end_distance:
                        q.append((next_point, next_distance))
                        
    reachable = len([v for v in visited.values() if v % 2 == end_mod])
    return reachable

a = get_reachable(STEP_REM)
b = get_reachable(STEP_REM + rows)
c = get_reachable(STEP_REM + 2*rows)

A = ((c-b) - (b-a)) // 2
B = (b - a) - 3*A
C = a - B - A

f = lambda x: A*x**2 + B*x + C
r = f(ceil(STEPS / rows))
             
print(r)