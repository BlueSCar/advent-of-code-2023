import portion as P
import re
from collections import deque
from math import prod

file = open("day19/input.txt")
file_parts = file.read().split("\n\n")

WORKFLOW_PATTERN = re.compile("(\w+)\{([^\}]+)\}")
EVAL_PATTERN = re.compile("(\w)([<|>])(\d+)")

def parse_workflow(wf: str):
    g = WORKFLOW_PATTERN.match(wf).groups()
    key = g[0]
    steps = [tuple(s.split(":")) for s in g[1].split(",")]
    
    return (key, steps)

workflows = dict([parse_workflow(l.strip()) for l in file_parts[0].split()])
permutations = []
starting = {
    "x": P.closed(1, 4000),
    "m": P.closed(1, 4000),
    "a": P.closed(1, 4000),
    "s": P.closed(1, 4000)
}

q = deque([("in", starting)])

def evaluate(workflow, combos: dict):
    for step in workflows[workflow]:
        combo_copy = combos.copy()
        
        step_input = None
        step_output = None
        
        if len(step) == 1:
            step_output = step[0]
        else:
            step_input = step[0]
            step_output = step[1]
            
        if step_input is not None:
            splits = EVAL_PATTERN.match(step_input).groups()
            if splits[1] == "<":
                combo_copy[splits[0]] = combo_copy[splits[0]] & P.closed(1, int(splits[2]) - 1)
                combos[splits[0]] = combos[splits[0]] & P.closed(int(splits[2]), 4000)
            elif splits[1] == ">":
                combos[splits[0]] = combos[splits[0]] & P.closed(1, int(splits[2]))
                combo_copy[splits[0]] = combo_copy[splits[0]] & P.closed(int(splits[2]) + 1, 4000)
                
        if step_output == "A":
            permutations.append(combo_copy)
        elif step_output == "R":
            continue
        else:
            q.append((step_output, combo_copy))

while q:
    workflow, combos = q.pop()
    evaluate(workflow, combos)
    
totals = 0
for p in permutations:
    totals += prod([(x[1].upper - x[1].lower + 1) for x in p.items()])

print(totals)