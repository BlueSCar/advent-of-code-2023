import re
from collections import deque

LINE_PATTERN = re.compile("(?P<module_type>\W)?(?P<module>\w+) -> (?P<neighbors>(?:\w+(?:, )?)+)")

file = open("day20/input.txt")
lines = [LINE_PATTERN.match(l.strip()).groupdict() for l in file.readlines()]

modules = {}
for l in lines:
    modules[l["module"]] = { "module_type": l["module_type"], "neighbors": l["neighbors"].split(", ") }
    if l["module_type"] == "%":
        modules[l["module"]]["state"] = False
    elif l["module_type"] == "&":
        modules[l["module"]]["state"] = {}
        
for m in modules:
    for n in modules[m]["neighbors"] :
        if n in modules and modules[n]["module_type"] == "&":
            modules[n]["state"][m] = False
            
highs = 0
lows = 0

for i in range(1000):
    q = deque([("button", "broadcaster", False)])
    while q:
        sender, receiver, high_pulse = q.popleft()
        
        if high_pulse:
            highs += 1
        else:
            lows += 1
            
        if receiver in modules:
            receiver_module = modules[receiver]
            if receiver_module["module_type"] == "%":
                if high_pulse:
                    continue
                
                next_pulse = not receiver_module["state"]
                receiver_module["state"] = not receiver_module["state"]
            elif receiver_module["module_type"] == "&":
                receiver_module["state"][sender] = high_pulse
                next_pulse = not all(receiver_module["state"].values())
            else:
                next_pulse = high_pulse
                
            for n in receiver_module["neighbors"]:
                q.append((receiver, n, next_pulse))
        else:
            continue
    
product = highs*lows
print(product)