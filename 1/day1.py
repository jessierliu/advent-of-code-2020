"""
Day 1
"""

import itertools
import math

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n')[:-1]
lines = [int(l) for l in lines]

combos = itertools.combinations(lines, 2)
for c in combos:
    if sum(c) == 2020:
        print(math.prod(c))
        break

combos = itertools.combinations(lines, 3)
for c in combos:
    if sum(c) == 2020:
        print(math.prod(c))
        break
