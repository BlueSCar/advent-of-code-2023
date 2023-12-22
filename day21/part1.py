import numpy as np
from collections import deque

DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]
STEPS = 64
STEP_MOD = STEPS % 2

file = open("day21/input.txt")
plot = [l.strip() for l in file.readlines()]
rows = len(plot)
cols = len(plot[0])

starting_point = None
for i in range(rows):
    s_index = plot[i].find("S")
    if s_index != -1:
        starting_point = (i, s_index)
        break

visited = {}
q = deque([(starting_point, 0)])
while q:
    point, distance = q.popleft()
    
    for d in DIRECTIONS:
        next_point = (point[0] + d[0], point[1] + d[1])
        if next_point[0] >= 0 and next_point[1] >= 0 and next_point[0] < rows and next_point[1] < cols and plot[next_point[0]][next_point[1]] != "#":
            next_distance = distance + 1
                
            
            if next_point not in visited:
                visited[next_point] = next_distance
                if next_distance < STEPS:
                    q.append((next_point, next_distance))
                    
reachable = len([v for v in visited.values() if v % 2 == STEP_MOD]) 
             
print(reachable)