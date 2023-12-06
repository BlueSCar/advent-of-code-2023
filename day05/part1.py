import re

file = open('day05/input.txt')
groups = file.read().split("\n\n")

seeds = [int(s) for s in re.findall("\d+", groups[0])]

maps = [{}]
for seed in seeds:
    mapping = maps[0]
    mapping[seed] = seed
    
for i in range(1, len(groups)):
    maps.append({})
    group = groups[i]
    lines = group.split("\n")
    for j in range(1, len(lines)):
        inputs = [int(n) for n in re.split("\s", lines[j])]
        dest_start = inputs[0]
        source_start = inputs[1]
        range_len = inputs[2]
        source_end = source_start + range_len
        
        for source in maps[i-1]:
            if source >= source_start and source < source_end:
                diff = source - source_start
                destination = dest_start + diff
                maps[i-1][source] = destination
                maps[i][destination] = destination

    for l in maps[i-1].values():
        if l not in maps[i]:
            maps[i][l] = l
            
closest = min(maps[-1].keys())

print(closest)