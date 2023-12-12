

file = open("day11/input.txt")
lines = [l.strip() for l in file.readlines()]

empty_rows = []
for i in range(len(lines)):
    line = lines[i]
    if line.find("#") == -1:
        empty_rows.append(i)
    
empty_columns = []
for i in range(len(lines[0])):
    col = "".join([l[i] for l in lines])
    if col.find("#") == -1:
        empty_columns.append(i)   
    
galaxies = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "#":
            galaxies.append((i,j))
            
distances = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        
        row_diff = 0
        if g1[0] > g2[0]:
            empties = [r for r in empty_rows if r in range(g2[0], g1[0])]
            row_diff = (g1[0] - g2[0]) + len(empties) * 1000000 - len(empties)
        else:
            empties = [r for r in empty_rows if r in range(g1[0], g2[0])]
            row_diff = (g2[0] - g1[0]) + len(empties) * 1000000 - len(empties)
        
        col_diff = 0
        if g1[1] > g2[1]:
            empties = [r for r in empty_columns if r in range(g2[1], g1[1])]
            col_diff = (g1[1] - g2[1]) + len(empties) * 1000000 - len(empties)
        else:
            empties = [r for r in empty_columns if r in range(g1[1], g2[1])]
            col_diff = (g2[1] - g1[1]) + len(empties) * 1000000 - len(empties)
            
        distances += (row_diff + col_diff)

print(distances)