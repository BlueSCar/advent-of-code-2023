import numpy as np
from collections import deque

file = open("day16/input.txt")
grid = [[c for c in l.strip()] for l in file.readlines()]

DIRECTIONS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

def get_energy(start):
    visited = set()         
    moves = deque([start])
    while moves:
        move = moves.pop()
        
        if move in visited:
            continue
        
        visited.add(move)
        next = tuple(np.add(np.array((move[0], move[1])), np.array((move[2], move[3]))))
        
        if next[0] >= 0 and next[1] >= 0 and next[1] < len(grid) and next[0] < len(grid[0]):
            next_symbol = grid[next[1]][next[0]]
            
            if next_symbol == '-' and move[3] != 0:
                if next + DIRECTIONS['L'] not in visited:
                    moves.append(next + DIRECTIONS['L'])
                
                if next + DIRECTIONS['R'] not in visited:
                    moves.append(next + DIRECTIONS['R'])
            elif next_symbol == '|' and move[2] != 0:
                if next + DIRECTIONS['U'] not in visited:
                    moves.append(next + DIRECTIONS['U'])
                
                if next + DIRECTIONS['D'] not in visited:
                    moves.append(next + DIRECTIONS['D'])
            elif next_symbol == '/':
                if next + (-move[3], -move[2]) not in visited:
                    moves.append(next + (-move[3], -move[2]))
            elif next_symbol == '\\':
                if next + (move[3], move[2]) not in visited:
                    moves.append(next + (move[3], move[2]))
            else:
                moves.append(next + (move[2], move[3]))

    energized = len(set([(v[0],v[1]) for v in visited])) - 1
    return energized

max_energy = 0
rows = len(grid)
columns = len(grid[0])

for i in range(columns):
    # downwards
    energy = get_energy((i, -1, 0, 1))
    if energy > max_energy:
        max_energy = energy
        
    # upwards
    energy = get_energy((i, rows, 0, -1))
    if energy > max_energy:
        max_energy = energy
        
for i in range(rows):
    # rightward
    energy = get_energy((-1, i, 1, 0))
    if energy > max_energy:
        max_energy = energy
        
    # leftward
    energy = get_energy((columns, i, -1, 0))
    if energy > max_energy:
        max_energy = energy

print(max_energy)