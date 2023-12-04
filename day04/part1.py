import re

LINE_PATTERN = re.compile("Card\s+\d+:([ \d]+)\|([ \d]+)")

def parse_line(line: str):
    matches = LINE_PATTERN.findall(line)[0]
    winners = [int(m) for m in re.split("\s+", matches[0].strip())]
    numbers = [int(m) for m in re.split("\s+", matches[1].strip())]
    
    matching_numbers = len([n for n in numbers if n in winners])
    if matching_numbers > 0:
        return 2**(matching_numbers - 1)
    else:
        return 0

file = open('day04/input.txt')
scores = [parse_line(l.strip()) for l in file.readlines()]

sum = sum(scores)

print(sum)