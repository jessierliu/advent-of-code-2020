"""
Day 2
"""

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n')[:-1]
lines = [l.split(' ') for l in lines]

valid = 0
new_valid = 0
for cur_pw in lines:

    letter = cur_pw[1].strip(':')
    amount = cur_pw[2].count(letter)
    rule = cur_pw[0].split('-')
    rule = [int(r) for r in rule]

    if amount >= rule[0] and amount <= rule[1]:
        valid += 1

    occurences = cur_pw[2][rule[0] - 1] + cur_pw[2][rule[1] - 1]
    if occurences.count(letter) == 1:
        new_valid += 1

print(valid)
print(new_valid)
