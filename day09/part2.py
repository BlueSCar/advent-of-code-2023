file = open("day09/input.txt")
sequences = [[int(n) for n in l.strip().split(' ')] for l in file.readlines()]

def find_previous_value(sequence):
    diffs = [(sequence[i] - sequence[i-1]) for i in range(1, len(sequence))]
    
    uniques = list(set(diffs))
    if len(uniques) == 1 and uniques[0] == 0:
        return sequence[0]
    else:
        return sequence[0] - find_previous_value(diffs)

previous_values = []

for s in sequences:
    previous_value = find_previous_value(s)
    previous_values.append(previous_value)
    
total = sum(previous_values)

print(total)