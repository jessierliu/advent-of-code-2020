"""
Day 6
"""

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n\n')
qsum, qs = 0, 0

for line in lines:
    line_split = line.strip('\n').split('\n')

    qs += len(''.join(set(''.join(line_split))))
    qsum += len(set(line_split[0]).intersection(*line_split[1:]))

print(qs)
print(qsum)
