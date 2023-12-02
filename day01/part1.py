import re


file = open('day01/input.txt')
lines = [re.findall("\d", l.strip()) for l in file.readlines()]

sum = sum([int(f'{l[0]}{l[-1]}') for l in lines])

print(sum)