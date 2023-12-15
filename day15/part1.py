def get_hash(step):
    current = 0
    for c in step:
        current += ord(c)
        current *= 17
        current %= 256
        
    return current

file = open("day15/input.txt")
hashes = [get_hash(step) for step in file.read().strip().split(",")]

total = sum(hashes)

print(total)