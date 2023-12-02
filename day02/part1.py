import re

config = dict(red=12, green=13, blue=14)
game_pattern = re.compile("Game (\d+):")
color_pattern = re.compile("(\d+) (red|blue|green)")

def get_line_value(line):
    game = game_pattern.findall(line)
    colors = color_pattern.findall(line)
    
    for color in colors:
        if int(color[0]) > config[color[1]]:
            return 0
    
    return int(game[0])

file = open('day02/input.txt')
lines = [l.strip() for l in file.readlines()]

sum = sum(get_line_value(l) for l in lines)

print(sum)