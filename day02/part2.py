import re

color_pattern = re.compile("(\d+) (red|blue|green)")

def get_line_value(line):
    colors = color_pattern.findall(line)
    
    line_values = dict(red=0, green=0, blue=0)
    
    for color in colors:
        number = int(color[0])
        color_type = color[1]
        
        if number > line_values[color_type]:
            line_values[color_type] = number
    
    return line_values['red'] * line_values['green'] * line_values['blue']

file = open('day02/input.txt')
lines = [l.strip() for l in file.readlines()]

sum = sum(get_line_value(l) for l in lines)

print(sum)