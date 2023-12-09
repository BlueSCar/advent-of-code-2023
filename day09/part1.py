file = open("day09/input.txt")
sequences = [[int(n) for n in l.strip().split(' ')] for l in file.readlines()]

def find_next_value(sequence):
    diffs = [(sequence[i] - sequence[i-1]) for i in range(1, len(sequence))]
    
    uniques = list(set(diffs))
    if len(uniques) == 1 and uniques[0] == 0:
        return sequence[-1]
    else:
        return sequence[-1] + find_next_value(diffs)

next_values = []

for s in sequences:
    next_value = find_next_value(s)
    next_values.append(next_value)
    
total = sum(next_values)

print(total)