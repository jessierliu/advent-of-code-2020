"""
Day 11
"""

from copy import deepcopy

with open('input.txt', 'r') as f:
    lines = f.read()
    lines = [list(l) for l in lines.strip('\n').split('\n')]


def adjacent_seats(r, c, seats):
    pos_rows = range(max(0, r - 1), min(len(seats) - 1, r + 1) + 1)
    pos_cols = range(max(0, c - 1), min(len(seats[r]) - 1, c + 1) + 1)

    adj = 0
    for row in pos_rows:
        for col in pos_cols:
            if row == r and col == c:
                continue

            if seats[row][col] == '#':
                adj += 1

    return adj


stop = False
while not stop:
    seat_copy = deepcopy(lines)
    for ro in range(len(seat_copy)):
        for co in range(len(seat_copy[0])):
            if seat_copy[ro][co] == 'L':
                if adjacent_seats(ro, co, seat_copy) == 0:
                    lines[ro][co] = '#'

            elif seat_copy[ro][co] == '#':
                if adjacent_seats(ro, co, seat_copy) >= 4:
                    lines[ro][co] = 'L'

    if sum(lines, []) == sum(seat_copy, []):
        stop = True

print(sum(lines, []).count('#'))

# part 2
with open('input.txt', 'r') as f:
    lines = f.read()
    lines = [list(l) for l in lines.strip('\n').split('\n')]


def first_seats(r, c, seats):
    types = []

    # check down
    for row in range(r + 1, len(lines)):
        if seats[row][c] != '.':
            types.append(seats[row][c])
            break

    # check up
    for row in reversed(range(r)):
        if seats[row][c] != '.':
            types.append(seats[row][c])
            break

    # check left
    for col in reversed(range(c)):
        if seats[r][col] != '.':
            types.append(seats[r][col])
            break

    # check right
    for col in range(c + 1, len(lines[r])):
        if seats[r][col] != '.':
            types.append(seats[r][col])
            break

    # check NW
    for row, col in zip(reversed(range(r)), reversed(range(c))):
        if seats[row][col] != '.':
            types.append(seats[row][col])
            break

    # check NE
    for row, col in zip(reversed(range(r)), range(c + 1, len(lines[r]))):
        if seats[row][col] != '.':
            types.append(seats[row][col])
            break

    # check SE
    for row, col in zip(range(r + 1, len(lines)), range(c + 1, len(lines[r]))):
        if seats[row][col] != '.':
            types.append(seats[row][col])
            break

    # check SW
    for row, col in zip(range(r + 1, len(lines)), reversed(range(c))):
        if seats[row][col] != '.':
            types.append(seats[row][col])
            break

    return types.count('#'), types


stop = False
while not stop:
    seat_copy = deepcopy(lines)
    for ro in range(len(seat_copy)):
        for co in range(len(seat_copy[0])):
            if seat_copy[ro][co] == 'L':
                if first_seats(ro, co, seat_copy)[0] == 0:
                    lines[ro][co] = '#'

            elif seat_copy[ro][co] == '#':
                if first_seats(ro, co, seat_copy)[0] >= 5:
                    lines[ro][co] = 'L'

    if sum(lines, []) == sum(seat_copy, []):
        stop = True

print(sum(lines, []).count('#'))
