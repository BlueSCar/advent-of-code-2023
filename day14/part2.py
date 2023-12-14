
file = open("day14/input.txt")
grid = [[r for r in l.strip()] for l in file.readlines()]

def cycle_grid():
    rows = len(grid)
    columns = len(grid[0])
    
    # shift north
    for i in range(columns):
        column = "".join([r[i] for r in grid])
        while ".O" in column:
            column = column.replace(".O", "O.")
            
        for j in range(rows):
            grid[j][i] = column[j]
            
    # shift west
    for i in range(rows):
        row = "".join(grid[i])
        while ".O" in row:
            row = row.replace(".O", "O.")
            
        for j in range(columns):
            grid[i][j] = row[j]
        
    #shift south
    for i in range(columns):
        column = "".join([r[i] for r in grid])
        while "O." in column:
            column = column.replace("O.", ".O")
            
        for j in range(rows):
            grid[j][i] = column[j]
            
    # shift east
    for i in range(rows):
        row = "".join(grid[i])
        while "O." in row:
            row = row.replace("O.", ".O")
            
        for j in range(columns):
            grid[i][j] = row[j]
        
def get_load(gr):
    grid_size = len(gr)
    return sum([len([j for j in gr[i] if j == "O"]) * (grid_size - i) for i in range(grid_size)])

def stringify_grid(gr):
    return "\n".join(["".join(l) for l in gr])
        
memory = []
first_occurrence = 0
next_occurrence = 0
for i in range(100000):
    cycle_grid()
    grid_string = stringify_grid(grid)
    if grid_string in memory:
        first_occurrence = memory.index(grid_string)
        next_occurrence = i
        break
    else:
        memory.append(grid_string)

diff = next_occurrence - first_occurrence
cycle = (1000000000 - (first_occurrence + 1)) % diff
g = memory[cycle + first_occurrence]

load = get_load([[r for r in l.strip()] for l in g.split("\n")])

print(load)