import math
import numpy as np

file = open("day10/input.txt")
lines = [l.strip() for l in file.readlines()]

S = None

for i in range(len(lines)):
    if S is not None:
        break;
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            S = (i, j)
            break
            
map = np.full([len(lines), len(lines[0])], np.Infinity)
map[S[0]][S[1]] = 0

current = (S[0], S[1])
previous = (S[0], S[1])
next = (S[0], S[1])
completed = False

if S[0] > 0 and lines[S[0] - 1][S[1]] in ['|', '7', 'F']:
    current = (S[0] - 1, S[1])
elif S[1] < len(lines[0]) - 1 and lines[S[0]][S[1] + 1] in ['-', '7', 'J']:
    current = (S[0], S[1] + 1)
elif S[0] < len(lines) - 1 and lines[S[0] + 1][S[1]] in ['|', 'L',' J']:
    current = (S[0] + 1, S[1])
else:
    current = (S[0], S[1] - 1)


while not completed:
    current_value = lines[current[0]][current[1]]
    if current_value == 'S':
        completed = True
    else:
        map[current[0]][current[1]] = map[previous[0]][previous[1]] + 1
        
        if current_value == '|':
            if previous[0] < current[0]:
                next = (current[0] + 1, current[1])
            else:
                next = (current[0] - 1, current[1])
        elif current_value == '-':
            if previous[1] < current[1]:
                next = (current[0], current[1] + 1)
            else:
                next = (current[0] , current[1] - 1)
        elif current_value == '7':
            if previous[0] == current[0]:
                next = (current[0] + 1, current[1])
            else:
                next = (current[0], current[1] - 1)
        elif current_value == 'F':
            if previous[0] == current[0]:
                next = (current[0] + 1, current[1])
            else:
                next = (current[0], current[1] + 1)
        elif current_value == 'J':
            if previous[0] == current[0]:
                next = (current[0] - 1, current[1])
            else:
                next = [current[0], current[1] - 1]
        elif current_value == 'L':
            if previous[0] == current[0]:
                next = (current[0] - 1, current[1])
            else:
                next = [current[0], current[1] + 1]
                
        previous = current
        current = next

cleaned = []
for i in range(len(lines)):
    row = []
    for j in range(len(lines[0])):
        if map[i][j] == np.Infinity:
            row.append(".")
        else:
            row.append(lines[i][j])
    
    cleaned.append(row)
    
enclosed = 0
                
for i in range(len(cleaned)):
    intersections = 0
    for j in range(len(cleaned) - i):
        symbol = cleaned[j][i+j]
        if symbol == "." and intersections % 2 == 1:
            # print(f'({j},{i+j})')
            enclosed += 1
        elif symbol in ["-","|","J","S","F"]:
            intersections += 1
            
for i in range(1, len(cleaned)):
    intersections = 0
    for j in range(len(cleaned) - i):
        symbol = cleaned[j+i][j]
        if symbol == "." and intersections % 2 == 1:
            # print(f'({i+j},{j})')
            enclosed += 1
        elif symbol in ["-","|","J","S","F"]:
            intersections += 1

print(enclosed)