from collections import Counter
from functools import cmp_to_key

CARDS = "J23456789TQKA"

def classify_hand(hand: str):
    grouped = Counter(hand)
    ordered = [g for g in grouped.most_common() if g[0] != 'J']
    uniques = len(ordered)
    
    if len(ordered) > 0:
        ordered[0] = (ordered[0][0], ordered[0][1] + grouped['J'])
    else:
        ordered.append(('J', grouped['J']))
    
    if uniques == 5:
        return 1
    elif uniques == 4:
        return 2
    elif uniques == 3:
        if ordered[0][1] == 3:
            return 4
        else:
            return 3
    elif uniques == 2:
        if ordered[0][1] == 4:
            return 6
        else:
            return 5
    else:
        return 7
    
def compare_hands(h1, h2):
    class_diff = h1['classification'] - h2['classification']
    if class_diff != 0:
        return class_diff
    else:
        for i in range(5):
            val_diff = CARDS.index(h1['hand'][i]) - CARDS.index(h2['hand'][i])
            if val_diff != 0:
                return val_diff
    
    return 0

file = open('day07/input.txt')
lines = [l.strip().split(' ') for l in file.readlines()]

hands = list()

for l in lines:
    bid = int(l[1])
    hand = l[0]
    classification = classify_hand(hand)
    
    hands.append(dict(hand=hand, classification=classification, bid=bid))
    
sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

totals = sum([(i+1)*h['bid'] for i, h in enumerate(sorted_hands)])

print(totals)