

file = open("day11/input.txt")
lines = [l.strip() for l in file.readlines()]

empty_rows = []
for i in range(len(lines)):
    line = lines[i]
    if line.find("#") == -1:
        empty_rows.append(i)
        
row_size = len(lines[0])
for i in range(len(empty_rows)):
    lines.insert(empty_rows[i] + i, "." * row_size)
    
empty_columns = []
for i in range(len(lines[0])):
    col = "".join([l[i] for l in lines])
    if col.find("#") == -1:
        empty_columns.append(i)
        
for i in range(len(empty_columns)):
    lines = [l[:(empty_columns[i] + i)] + "." + l[(empty_columns[i] + i):] for l in lines]
    
    
galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            galaxies.append((i,j))
            
distances = []
for i in range(len(galaxies) - 1):
    for j in range(i, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        
        distance = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
        distances.append(distance)

total = sum(distances)

print(total)