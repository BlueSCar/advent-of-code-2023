import re
from collections import OrderedDict

STEP_PATTERN = re.compile("(\w+)(=|-)(\d+)?")

def get_box(step):
    current = 0
    for c in step:
        current += ord(c)
        current *= 17
        current %= 256
        
    return current

file = open("day15/input.txt")
steps = [step for step in file.read().strip().split(",")]

boxes = [OrderedDict() for i in range(256)]
for step in steps:
    parts = STEP_PATTERN.match(step)
    box = get_box(parts[1])
    
    if parts[2] == "-":
        if parts[1] in boxes[box]:
            boxes[box].pop(parts[1])
    else:
        boxes[box][parts[1]] = int(parts[3])
        
power = 0
for i in range(len(boxes)):
    lenses = list(boxes[i].values())
    for j in range(len(lenses)):
        power += (i + 1)*(j + 1)*(lenses[j])

print(power)