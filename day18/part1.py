import re

DIRECTION_PATTERN = re.compile("(\w) (\d+) \((#\w{6})\)")
DIRECTIONS = {
    'D': (0, 1),
    'R': (1, 0),
    'U': (0, -1),
    'L': (-1, 0)
}

file = open("day18/input.txt")
lines = [DIRECTION_PATTERN.match(l.strip()).groups() for l in file.readlines()]

x = 0
y = 0

area = 1 #starting block
perimeter = 0

for line in lines:
    d = DIRECTIONS[line[0]]
    
    nx = x + d[0]*int(line[1])
    ny = y + d[1]*int(line[1])
    
    det = x*ny - y*nx
    area += (det / 2) + float(line[1]) / 2 #determinant + perimeter blocks
    
    x = nx
    y = ny
    

print(int(area))