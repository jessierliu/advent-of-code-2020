"""
Day 24
"""

from copy import deepcopy

with open('input.txt', 'r') as f:
    ops = f.read()

ops = ops.strip('\n').split('\n')
dirs = {
    'e': [0, 2],
    'w': [0, -2],
    'se': [1, 1],
    'sw': [1, -1],
    'ne': [-1, 1],
    'nw': [-1, -1]
}

# 1 for white, 0 for black
hexgrid = {(0, 0): 1}

# part 1
for op in ops:
    r, c = 0, 0
    while len(op) != 0:
        for d, move in dirs.items():
            if op.startswith(d):
                op = op[len(d):]
                r += move[0]
                c += move[1]

    # flip the tile
    key = (r, c)
    try:
        if hexgrid[key] == 1:
            hexgrid[key] = 0
        else:
            hexgrid[key] = 1
    except KeyError:
        hexgrid[key] = 0

print('Part 1:', list(hexgrid.values()).count(0))

# part 2
new_tiles = deepcopy(hexgrid)
for i in range(100):
    add_tiles = deepcopy(new_tiles)
    for (r, c), color in new_tiles.items():
        for move in dirs.values():
            try:
                new_tiles[(r + move[0], c + move[1])]
            except KeyError:
                add_tiles[(r + move[0], c + move[1])] = 1

    new_tiles = deepcopy(add_tiles)
    for (r, c), color in add_tiles.items():

        adjacent = []
        for move in dirs.values():
            try:
                adjacent.append(add_tiles[(r + move[0], c + move[1])])
            except KeyError:
                pass

        if color == 0 and (adjacent.count(0) == 0 or adjacent.count(0) > 2):
            new_tiles[(r, c)] = 1

        elif color == 1 and adjacent.count(0) == 2:
            new_tiles[(r, c)] = 0

print('Part 2:', list(new_tiles.values()).count(0))
