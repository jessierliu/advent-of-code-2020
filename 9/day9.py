"""
Day 9
"""

from itertools import combinations

with open('input.txt', 'r') as f:
    lines = f.read()
    lines = [int(i) for i in lines.strip('\n').split('\n')]

step = 25
for idx in range(step, len(lines)):

    possible_sums = [sum(c) for c in combinations(lines[(idx - step):idx], 2)]
    if possible_sums.count(lines[idx]) == 0:
        key = lines[idx]
        print(key)
        break

for contig in range(2, len(lines) - 1):
    for idx in range(len(lines) - contig + 1):
        potential = lines[idx:(idx + contig)]
        if sum(potential) == key:
            print(min(potential) + max(potential))
            break
