import numpy as np

from heapq import heappop, heappush

file = open("day17/test.txt")
grid = [[int(c) for c in l.strip()] for l in file.readlines()]

DIRECTIONS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

rows = len(grid)
columns = len(grid[0])

distances = np.full((rows, columns), np.Infinity)
visited = { (0, 0, None, 0): 0 }
q = [(0, 0, None, 0, 0)]

while q:
    x, y, previous_direction, repeats, distance = heappop(q)
    
    for key in DIRECTIONS:
        if repeats < 3 or key != previous_direction:
            direction = DIRECTIONS[key]
            next_repeats = 0
            if key == previous_direction:
                next_repeats = repeats + 1
                
            if previous_direction is None or direction != (-DIRECTIONS[previous_direction][0], -DIRECTIONS[previous_direction][1]):
                nx, ny = tuple(np.array((x,y)) + np.array(direction))
                
                if nx >= 0 and nx < columns and ny >= 0 and ny < rows:
                    next_distance = distance + grid[ny][nx]
                    n = (nx, ny, key, next_repeats, next_distance)
                
                    if nx == columns - 1 and ny == rows - 1:
                        print()
                    
                    if n[:-1] not in visited or next_distance < visited[n[:-1]]:
                        visited[n[:-1]] = next_distance
                        if next_distance < distances[ny][nx]:
                            distances[ny][nx] = next_distance
                            heappush(q, n)
                    
print()