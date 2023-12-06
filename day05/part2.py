import portion as P
import re

file = open('day05/input.txt')
groups = file.read().split("\n\n")

pairs = [s for s in re.findall("(\d+) (\d+)", groups[0])]

intervals = P.empty()
for pair in pairs:
    interval = P.closedopen(int(pair[0]), int(pair[0]) + int(pair[1]))
    intervals = intervals | interval
    
for g in groups[1:]:
    next_intervals = P.empty()
    visited_intervals = P.empty()
    
    lines = g.split("\n")
    for l in lines[1:]:
        inputs = [int(n) for n in re.split("\s", l)]
        dest_start = inputs[0]
        source_start = inputs[1]
        range_len = inputs[2]
        source_end = source_start + range_len
        diff = dest_start - source_start
        
        source_interval = P.closedopen(source_start, source_end) & intervals
        visited_intervals = source_interval | visited_intervals
        
        for s in source_interval:
            next_intervals = next_intervals | P.closedopen(s.lower + diff, s.upper + diff)
            
    leftover = intervals - visited_intervals
    next_intervals = next_intervals | leftover
    
    intervals = next_intervals
        
    
print(intervals.lower)