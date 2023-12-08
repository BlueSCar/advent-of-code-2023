import re

NODE_PATTERN = re.compile("(\w{3}) = \((\w{3}), (\w{3})\)")

file = open("day08/input.txt")
lines = [l.strip() for l in file.readlines()]

instructions = lines[0]
num_instructions = len(instructions)

order = 'LR'

map = {}

for l in lines[2:]:
    m = NODE_PATTERN.fullmatch(l)
    
    map[m[1]] = (m[2], m[3])
    

current_pos = "AAA"
steps = 0

while current_pos != "ZZZ":
    direction = instructions[steps % num_instructions]
    current_pos = map[current_pos][order.index(direction)]
    steps += 1

print(steps)