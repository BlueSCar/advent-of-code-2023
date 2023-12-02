import re

pattern = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

mappings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def get_numeric(digit):
    if digit in mappings:
        return mappings[digit]

    return digit

file = open('day01/input.txt')
lines = [re.findall(pattern, l.strip()) for l in file.readlines()]

sum = sum([int(f'{get_numeric(l[0])}{get_numeric(l[-1])}') for l in lines])

print(sum)