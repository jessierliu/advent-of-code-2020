"""
Day 10
"""

with open('input.txt', 'r') as f:
    lines = f.read()
    lines = sorted([int(i) for i in lines.strip('\n').split('\n')])

lines.insert(0, 0)
lines.append(lines[-1] + 3)
ld = [j - i for i, j in zip(lines[:-1], lines[1:])]
print(ld.count(1) * ld.count(3))

combos_up_to_index = [1] * len(lines)
for i in range(1, len(lines)):

    combos_up_to_index[i] = combos_up_to_index[i - 1]

    if i > 1 and lines[i] - lines[i - 2] <= 3:
        combos_up_to_index[i] += combos_up_to_index[i - 2]

    if i > 2 and lines[i] - lines[i - 3] <= 3:
        combos_up_to_index[i] += combos_up_to_index[i - 3]
print(combos_up_to_index[-1])
