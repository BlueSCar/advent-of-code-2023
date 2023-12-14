
file = open("day14/input.txt")
grid = [[c for c in l.strip()] for l in file.readlines()]

for i in range(len(grid[0])):
    column = "".join([r[i] for r in grid])
    while ".O" in column:
        column = column.replace(".O", "O.")
        
    for j in range(len(grid)):
        grid[j][i] = column[j]
       
grid_size = len(grid)
load = sum([len([j for j in grid[i] if j == "O"]) * (grid_size - i) for i in range(grid_size)])

print(load)