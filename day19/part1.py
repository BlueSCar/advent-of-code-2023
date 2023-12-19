import re

file = open("day19/input.txt")
file_parts = file.read().split("\n\n")

PART_PATTERN = re.compile("(?:([xmas])=(\d+))")
WORKFLOW_PATTERN = re.compile("(\w+)\{([^\}]+)\}")

def parse_workflow(wf: str):
    g = WORKFLOW_PATTERN.match(wf).groups()
    key = g[0]
    steps = [tuple(s.split(":")) for s in g[1].split(",")]
    
    return (key, steps)

workflows = dict([parse_workflow(l.strip()) for l in file_parts[0].split()])
parts = [dict([(k, int(v)) for (k, v) in PART_PATTERN.findall(l.strip())]) for l in file_parts[1].split()]

accepted = []
rejected = []

def run_workflow(name, part):
    steps = workflows[name]
    for step in steps:
        step_input = None
        step_output = None
        
        if (len(step)) == 1:
            step_output = step[0]
        else:
            step_input = step[0]
            step_output = step[1]
            
        if step_input is not None:
            if not eval(step_input, part):
                continue
        
        if step_output == "A":
            accepted.append(part)
        elif step_output == "R":
            rejected.append(part)
        else:
            run_workflow(step_output, part)
        break
                
for part in parts:
    run_workflow("in", part)

total = sum([p[k] for p in accepted for k in p if k in "xmas"])    

print(total)