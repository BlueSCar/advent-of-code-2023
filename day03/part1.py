import re

def is_part_number(match: re.Match, line: str, previous: str, next: str):
    start = match.start()
    if start > 0:
        start -= 1
        
    end = match.end()
    if end < len(line) - 1:
        end += 1
        
    if re.search("[^\d.]", line[start:end]) or (previous is not None and re.search("[^\d.]", previous[start:end])) or (next is not None and re.search("[^\d.]", next[start:end])):
        return True
    else:
        return False

file = open('day03/input.txt')
lines = [l.strip() for l in file.readlines()]

part_nos = []

for i in range(len(lines)):
    line = lines[i]
    
    if i > 0:
        previous = lines[i - 1]
    else:
        previous = None
    
    if i < len(lines) - 1:
        next = lines[i + 1]
        
    matches = re.finditer("\d+", lines[i])
    for m in matches:
        if is_part_number(m, line, previous, next):
            part_nos.append(int(m[0]))
            
sum = sum(part_nos)

print(sum)