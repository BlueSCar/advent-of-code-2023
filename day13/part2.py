

file = open("day13/input.txt")
patterns = file.read().split("\n\n")

def find_line(rows):
    for i in range(1, len(rows)):
        deviations = []
        size = min([i, len(rows) - i])
        for j in range(size):
            x = rows[i - j - 1]
            y = rows[i + j]
            
            if x == y:
                deviations.append(0)
            else:
                deviations.append(sum(1 for (a, b) in zip(x, y) if a != b))
        
        if sum(deviations) == 1:
            return i
    
    return 0

def get_value(pattern):
    lines = pattern.splitlines()
    row_value = find_line(lines) * 100
    
    column_value = 0
    if row_value == 0:
        columns = ["".join([l[i] for l in lines]) for i in range(len(lines[0]))]
        column_value = find_line(columns)
    
    return row_value + column_value

total = 0
for pattern in patterns:
    value = get_value(pattern)
    total += value

print(total)