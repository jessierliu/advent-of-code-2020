"""
Day 5
"""

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n')[:-1]
total_rows = 128
total_cols = 8
sids = []

for board_pass in lines:

    pos_rows = list(range(total_rows))
    pos_cols = list(range(total_cols))

    for i in range(7):
        if board_pass[i] == 'F':
            pos_rows = pos_rows[:int(len(pos_rows) / 2)]
        else:
            pos_rows = pos_rows[int(len(pos_rows) / 2):]

    for i in range(7, 10):
        if board_pass[i] == 'L':
            pos_cols = pos_cols[:int(len(pos_cols) / 2)]
        else:
            pos_cols = pos_cols[int(len(pos_cols) / 2):]

    sids.append(pos_rows[0] * 8 + pos_cols[0])

print(max(sids))
print(set(list(range(min(sids), max(sids)))) - set(sids))
