"""
Day 21
"""

import regex

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.strip('\n').split('\n')

all_ing = []
unique_alg = {}
for line in lines:
    reg = regex.search('(.*) [(]contains (.*)[)]', line)
    ing, alg = reg.group(1), reg.group(2)
    all_ing.append(ing.split())

    for a in alg.split(', '):
        if a in unique_alg.keys():
            unique_alg[a] &= set(ing.split())
        else:
            unique_alg[a] = set(ing.split())

# part 1
all_alg = set([i for ing in unique_alg.values() for i in ing])
not_alg = [i not in all_alg for ing in all_ing for i in ing]
print(sum(not_alg))

# part 2
true_alg = {}
while len(true_alg.keys()) != len(unique_alg.keys()):

    for key, val in unique_alg.items():
        if len(val) == 1 and key not in true_alg.keys():
            true_alg[key] = val

        elif len(val) > 1 and key not in true_alg.keys():
            for tval in true_alg.values():
                val -= tval
            unique_alg[key] = val

ci = []
for alg, ing in sorted(true_alg.items()):
    ci.append(str(list(ing)[0]))

print(','.join(ci))
