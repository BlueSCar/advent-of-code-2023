import functools

file = open("day12/input.txt")
lines = [l.split() for l in file.readlines()]

@functools.cache
def get_matches(pattern, groups):
    if len(groups) == 0:
        if "#" in pattern:
            return 0
        else:
            return 1
    
    minimum_size = len(groups) + sum(groups) - 1
    cushion = len(pattern) - minimum_size + 1
    
    first = groups[0]
    rest = groups[1:]
    
    matches = 0
    
    for c in range(cushion):
        part = f"{'.' * c}{'#' * first}."
        if len([(x,y) for (x,y) in zip(pattern, part) if x != y and x != "?"]) == 0:
            matches += get_matches(pattern[len(part):], rest)
        
    return matches

all_matches = 0
for l in lines:
    pattern = l[0]
    groups = tuple(map(int, l[1].split(",")))
    
    m =  get_matches(pattern, groups)
    all_matches += m

print(all_matches)