from heapq import heappop, heappush

file = open("day17/input.txt")
grid = [[int(c) for c in l.strip()] for l in file.readlines()]

DIRECTIONS = {
    'D': (0, 1),
    'R': (1, 0),
    'U': (0, -1),
    'L': (-1, 0)
}

rows = len(grid)
columns = len(grid[0])

q = [(0, 0, 0, -1)]
visited = set()
distances = {}

while q:
    d, x, y, last = heappop(q)
    if x == rows - 1 and y == columns - 1:
        print(d)
        break
    
    if (x, y, last) not in visited:
        visited.add((x, y, last))
        for key in DIRECTIONS:
            direction = DIRECTIONS[key]
            distance_added = 0
            if key != last and (last not in DIRECTIONS or (direction[0] + DIRECTIONS[last][0]) != 0 or (direction[1] + DIRECTIONS[last][1]) != 0):
                for step in range(1, 11):
                    nx = x + direction[0] * step
                    ny = y + direction[1] * step
                    if nx >= 0 and ny >= 0 and nx < rows and ny < columns:
                        distance_added += grid[nx][ny]
                        if step >= 4:
                            nd = d + distance_added
                            if nd < distances.get((nx, ny, key), 1e100):
                                distances[(nx, ny, key)] = nd
                                heappush(q, (nd, nx, ny, key))

print()