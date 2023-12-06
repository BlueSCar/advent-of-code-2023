import math
import re

file = open('day06/input.txt')
lines = [l.strip() for l in file.readlines()]

times = [int(t) for t in re.split("\s+", lines[0])[1:]]
distances = [int(d) for d in re.split("\s+", lines[1])[1:]]

num_solutions = []

for i in range(len(times)):
    time = times[i]
    distance = distances[i]
    
    discriminant = math.sqrt(time**2 - 4*distance)
    
    solution1 = math.floor((-time + discriminant) / -2)
    solution2 = math.ceil((-time - discriminant) / -2)
    
    num_solutions.append(abs(solution1 - solution2) - 1)

product = math.prod(num_solutions)

print(product)