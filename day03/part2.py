import re

def get_adjacent_parts(match: re.Match, line: str, previous: str, next: str):
    start = match.start()
    if start > 0:
        start -= 1
        
    end = match.end()
        
    part_nos = []
        
    adjacent_lines = [line]
    if previous is not None:
        adjacent_lines.append(previous)
    if next is not None:
        adjacent_lines.append(next)
        
    for l in adjacent_lines:
        for n in re.finditer("\d+", l):
            if n.start() <= end and (n.end() - 1) >= start:
                part_nos.append(int(n[0]))
                
    return part_nos

file = open('day03/input.txt')
lines = [l.strip() for l in file.readlines()]

gear_ratios = []

for i in range(len(lines)):
    line = lines[i]
    
    if i > 0:
        previous = lines[i - 1]
    else:
        previous = None
    
    if i < len(lines) - 1:
        next = lines[i + 1]
        
    matches = re.finditer("\*", lines[i])
    for m in matches:
        parts = get_adjacent_parts(m, line, previous, next)
        if (len(parts) == 2):
            gear_ratios.append(parts[0] * parts[1])
            
sum = sum(gear_ratios)

print(sum)