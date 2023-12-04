import re

LINE_PATTERN = re.compile("Card\s+(\d+):([ \d]+)\|([ \d]+)")

games = dict()

def parse_line(line: str):
    matches = LINE_PATTERN.findall(line)[0]
    winners = [int(m) for m in re.split("\s+", matches[1].strip())]
    numbers = [int(m) for m in re.split("\s+", matches[2].strip())]
    
    matching_numbers = len([n for n in numbers if n in winners])
    
    return dict(
        occurrences=1,
        matches=matching_numbers
    )

file = open('day04/input.txt')
cards = [parse_line(l.strip()) for l in file.readlines()]

for i in range(len(cards)):
    if cards[i]['matches'] > 0:
        for j in range(i+1, min([i+cards[i]['matches']+1, len(cards)])):
            cards[j]['occurrences'] += cards[i]['occurrences']
            
total_cards = sum([c['occurrences'] for c in cards])

print(total_cards)