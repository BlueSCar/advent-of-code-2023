import math
import re

file = open('day06/input.txt')
lines = [l.strip() for l in file.readlines()]

time = int("".join([t for t in re.split("\s+", lines[0])[1:]]))
distance = int("".join([d for d in re.split("\s+", lines[1])[1:]]))

discriminant = math.sqrt(time**2 - 4*distance)

solution1 = math.floor((-time + discriminant) / -2)
solution2 = math.ceil((-time - discriminant) / -2)

num_solutions = abs(solution1 - solution2) - 1

print(num_solutions)