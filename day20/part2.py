import re
from collections import deque
from itertools import count
from math import lcm

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
    for n in modules[m]["neighbors"]:
        if n in modules and modules[n]["module_type"] == "&":
            modules[n]["state"][m] = False
    
def propagate_pulse(modules, sender, receiver, high_pulse):
    if receiver in modules:
            receiver_module = modules[receiver]
            if receiver_module["module_type"] == "%":
                if high_pulse:
                    return
                
                next_pulse = not receiver_module["state"]
                receiver_module["state"] = not receiver_module["state"]
            elif receiver_module["module_type"] == "&":
                receiver_module["state"][sender] = high_pulse
                next_pulse = not all(receiver_module["state"].values())
            else:
                next_pulse = high_pulse
                
            for n in receiver_module["neighbors"]:
                yield receiver, n, next_pulse

def find_periods(modules):
    periodic = set()
    for m in modules:
        if modules[m]["neighbors"] == ['rx']:
            rx_source = m
            break
 
    for m in modules:
        if rx_source in modules[m]["neighbors"]:
            periodic.add(m)

    for iteration in count(1):
        q = deque([('button', 'broadcaster', False)])

        while q:
            sender, receiver, pulse = q.popleft()

            if not pulse:
                if receiver in periodic:
                    yield iteration

                    periodic.discard(receiver)
                    if not periodic:
                        return

            q.extend(propagate_pulse(modules, sender, receiver, pulse))

lcm = lcm(*find_periods(modules))
print(lcm)