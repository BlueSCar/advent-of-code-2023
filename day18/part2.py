import re

DIRECTION_PATTERN = re.compile("(\w) (\d+) \(#(\w{5})(\w)\)")
DIRECTIONS = {
    '0': (1, 0),
    '1': (0, 1),
    '2': (-1, 0),
    '3': (0, -1)
}

file = open("day18/input.txt")
lines = [DIRECTION_PATTERN.match(l.strip()).groups() for l in file.readlines()]

x = 0
y = 0

area = 1 #starting block
perimeter = 0

for line in lines:
    d = DIRECTIONS[line[3]]
    distance = int(line[2], 16)
    
    nx = x + d[0]*distance
    ny = y + d[1]*distance
    
    det = x*ny - y*nx
    area += (det / 2) + distance / 2 #determinant + perimeter blocks
    
    x = nx
    y = ny
    

print(int(area))