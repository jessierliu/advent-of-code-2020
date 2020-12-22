"""
Day 20
"""

import numpy as np
import regex

directions = {
    '-1,0': 'top',
    '0,1': 'right',
    '1,0': 'bottom',
    '0,-1': 'left'
}


def match(current, new, direction=None):
    """
    direction is for the current one
    current is the one we're on
    """
    is_match = False
    if direction == 'bottom':
        if all(current[-1, :] == new[0, :]):
            is_match = True
    elif direction == 'top':
        if all(current[0, :] == new[-1, :]):
            is_match = True
    elif direction == 'left':
        if all(current[:, 0] == new[:, -1]):
            is_match = True
    elif direction == 'right':
        if all(current[:, -1] == new[:, 0]):
            is_match = True
    return is_match


with open('input.txt', 'r') as f:
    lines = f.read().strip('\n').split('\n\n')

tiles = {}
for line in lines:
    tile_num = regex.search('Tile ([0-9]*)', line).group(1)
    tile_img = line.split(':')[1].strip('\n').split('\n')
    tile_img = [list(row) for row in tile_img]
    tiles[tile_num] = np.stack(tile_img, axis=0)

num_tiles = len(tiles.keys())
row = col = int(np.sqrt(num_tiles))

# possible = permutations(tiles.keys(), num_tiles)
# for combo in possible:
#     combo = np.array(combo).reshape((row, col))
#
#     try:
#         for r in range(row):
#             for c in range(col):
#                 cur_tile = tiles[combo[r, c]]
#
#                 valid_search = []
#                 for (dr, dc) in product([0, -1, 1], repeat=2):
#                     if abs(dr + dc) == 1 and (0 <= r + dr < row) and \
#                             (0 <= c + dc < col):
#                         valid_search.append((dr, dc))
#
#                 num_matches = 0
#                 for (dr, dc) in valid_search:
#                     new_tile = tiles[combo[r + dr, c + dc]]
#                     dir = directions[f'{dr},{dc}']
#
#                     if not match(cur_tile, new_tile, dir):
#                         raise ValueError
#
#         print('all matches')
#         print(combo)
#         raise KeyError
#
#     except ValueError:
#         pass
#
#     except KeyError:
#         break

# part 1
borders = {}
for key, val in tiles.items():
    borders[key] = [val[0, :], val[-1, :], val[:, 0], val[:, -1]]

border_matches = [0 for _ in borders.keys()]
for i, (border_key, border_val) in enumerate(borders.items()):

    for key, val in borders.items():

        if key == border_key:
            continue

        for bval in border_val:
            m = []
            for b in val:
                if (bval == b).all():
                    m.append(True)
                else:
                    m.append(False)

                if (bval == np.flip(b)).all():
                    m.append(True)
                else:
                    m.append(False)

            if any(m):
                border_matches[i] += 1

corners = []
for m, key in zip(border_matches, borders.keys()):
    if m == 2:
        corners.append(int(key))
print(np.prod(corners))
