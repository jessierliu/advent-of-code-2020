"""
Day 20
"""

import time
from copy import deepcopy

import numpy as np
import regex

# directions = {
#     '-1,0': 'left',
#     '0,1': 'right',
#     '1,0': 'bottom',
#     '0,-1': 'top'
# }
directions = {
    '0,-1': 'left',
    '0,1': 'right',
    '1,0': 'bottom',
    '-1,0': 'top'
}


def remove_border(tile):
    new_tile = np.copy(tile)
    new_tile = new_tile[1:-1, 1:-1]
    return new_tile


def array_to_string(data):
    new = [''.join(list(data[r, :])) for r in range(data.shape[0])]
    return new


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


part1_time = time.time()
with open('input.txt', 'r') as f:
    lines = f.read().strip('\n').split('\n\n')

tiles = {}
for line in lines:
    tile_num = regex.search('Tile ([0-9]*)', line).group(1)
    tile_img = line.split(':')[1].strip('\n').split('\n')
    tile_img = [list(row) for row in tile_img]
    tiles[tile_num] = np.stack(tile_img, axis=0)

new_tiles = deepcopy(tiles)

num_tiles = len(tiles.keys())
row = col = int(np.sqrt(num_tiles))

# part 1
borders = {}
for key, val in tiles.items():
    # top, bottom, left, right
    borders[key] = [val[0, :], val[-1, :], val[:, 0], val[:, -1]]

border_matches = [0 for _ in borders.keys()]
which_matches, which_inds = {}, {}
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

                if (np.flip(bval) == b).all():
                    m.append(True)
                else:
                    m.append(False)

            if any(m):
                border_matches[i] += 1

                try:
                    which_inds[border_key].append(m.index(True))
                    which_matches[border_key].append(key)
                except KeyError:
                    which_matches[border_key] = [key]
                    which_inds[border_key] = [m.index(True)]
# part 1
corners = []
for m, key in zip(border_matches, borders.keys()):
    if m == 2:
        corners.append(int(key))
print('Part 1:', np.prod(corners))
print(f'Runtime: {time.time() - part1_time:0.2f} s.')

# part 2
part2_time = time.time()
print('\nStarting Part 2...')
full_tile_nums = np.zeros((row, col))

# fill in the border
print('figuring out border tile numbers...')
border_tiles = [str(corners[0])]
perimeter = 2 * row + 2 * col - 4
while len(border_tiles) < perimeter:
    for tile, match_tiles in which_matches.items():

        if tile == border_tiles[-1]:
            continue
        if len(match_tiles) in [2, 3]:
            if border_tiles[-1] in match_tiles and tile not in border_tiles:
                border_tiles.append(tile)

full_tile_nums[0, :] = border_tiles[:col]
full_tile_nums[:, -1] = border_tiles[col - 1:col + row - 1]
full_tile_nums[-1, :] = list(reversed(border_tiles[col + row - 2:-(row - 2)]))
full_tile_nums[1:, 0] = list(reversed(border_tiles[-(row - 1):]))

# figure out which borders dont match anything for corners
outer_edges = {}
for corner in border_tiles:
    matches = [False for _ in range(len(borders[str(corner)]))]
    for i, corner_border in enumerate(borders[str(corner)]):
        for tile_match in which_matches[str(int(corner))]:
            for bval in borders[tile_match]:
                if (bval == corner_border).all():
                    matches[i] = True
                elif (np.flip(bval) == corner_border).all():
                    matches[i] = True
    outer_edges[corner] = np.where(np.array(matches) == False)[0]

for c in range(1, col - 1):
    # top row
    tile_key = str(int(full_tile_nums[0, c]))
    no_edge = outer_edges[tile_key][0]

    if no_edge == 1:
        new_tiles[tile_key] = np.flipud(new_tiles[tile_key])
    elif no_edge == 0:
        pass
    elif no_edge == 2:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 3)
    elif no_edge == 3:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 1)

    # bottom row
    tile_key = str(int(full_tile_nums[-1, c]))
    no_edge = outer_edges[tile_key][0]

    if no_edge == 1:
        pass
    elif no_edge == 0:
        new_tiles[tile_key] = np.flipud(new_tiles[tile_key])
    elif no_edge == 2:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 1)
    elif no_edge == 3:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 3)

for r in range(1, row - 1):
    # left row
    tile_key = str(int(full_tile_nums[r, 0]))
    no_edge = outer_edges[tile_key][0]

    if no_edge == 3:
        new_tiles[tile_key] = np.fliplr(new_tiles[tile_key])
    elif no_edge == 2:
        pass
    elif no_edge == 1:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 3)
    elif no_edge == 0:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 1)

    # right row
    tile_key = str(int(full_tile_nums[r, -1]))
    no_edge = outer_edges[tile_key][0]

    if no_edge == 2:
        new_tiles[tile_key] = np.fliplr(new_tiles[tile_key])
    elif no_edge == 3:
        pass
    elif no_edge == 1:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 1)
    elif no_edge == 0:
        new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 3)

print('placing border tiles...')
# set the corner orientations
# for r, c in [[0, 0], [0, -1], [-1, -1], [-1, 0]]
r, c = 0, 0
tile_key = str(int(full_tile_nums[r, c]))
no_edge = outer_edges[tile_key]
if set(no_edge) == set([1, 2]):
    new_tiles[tile_key] = np.flipud(new_tiles[tile_key])
elif set(no_edge) == set([1, 3]):
    new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 2)
elif set(no_edge) == set([0, 2]):
    pass
elif set(no_edge) == set([0, 3]):
    new_tiles[tile_key] = np.fliplr(new_tiles[tile_key])

r, c = 0, -1
tile_key = str(int(full_tile_nums[r, c]))
no_edge = outer_edges[tile_key]
if set(no_edge) == set([1, 2]):
    new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 2)
elif set(no_edge) == set([1, 3]):
    new_tiles[tile_key] = np.flipud(new_tiles[tile_key])
elif set(no_edge) == set([0, 2]):
    new_tiles[tile_key] = np.fliplr(new_tiles[tile_key])
elif set(no_edge) == set([0, 3]):
    pass

r, c = -1, -1
tile_key = str(int(full_tile_nums[r, c]))
no_edge = outer_edges[tile_key]
if set(no_edge) == set([1, 2]):
    new_tiles[tile_key] = np.fliplr(new_tiles[tile_key])
elif set(no_edge) == set([1, 3]):
    pass
elif set(no_edge) == set([0, 2]):
    new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 2)
elif set(no_edge) == set([0, 3]):
    new_tiles[tile_key] = np.flipud(new_tiles[tile_key])

r, c = -1, 0
tile_key = str(int(full_tile_nums[r, c]))
no_edge = outer_edges[tile_key]
if set(no_edge) == set([1, 2]):
    pass
elif set(no_edge) == set([1, 3]):
    new_tiles[tile_key] = np.fliplr(new_tiles[tile_key])
elif set(no_edge) == set([0, 2]):
    new_tiles[tile_key] = np.flipud(new_tiles[tile_key])
elif set(no_edge) == set([0, 3]):
    new_tiles[tile_key] = np.rot90(new_tiles[tile_key], 2)

# go through possible orientations
full_img = [[None for _ in range(col)] for _ in range(row)]
corner_key = str(int(full_tile_nums[0, 0]))
next_key = str(int(full_tile_nums[0, 1]))
if match(new_tiles[corner_key], new_tiles[next_key], direction='right'):
    full_img[0][0] = new_tiles[corner_key]
    full_img[0][1] = new_tiles[next_key]
elif match(new_tiles[corner_key].T, new_tiles[next_key], direction='right'):
    full_img[0][0] = new_tiles[corner_key].T
    full_img[0][1] = new_tiles[next_key]
elif match(new_tiles[corner_key].T, np.fliplr(new_tiles[next_key]),
           direction='right'):
    full_img[0][0] = new_tiles[corner_key].T
    full_img[0][1] = np.fliplr(new_tiles[next_key])
elif match(new_tiles[corner_key], np.fliplr(new_tiles[next_key]),
           direction='right'):
    full_img[0][0] = new_tiles[corner_key]
    full_img[0][1] = np.fliplr(new_tiles[next_key])

for c in range(1, col - 1):
    # top row
    tile_key = str(int(full_tile_nums[0, c]))
    prev_tile = full_img[0][c - 1]
    if match(new_tiles[tile_key], prev_tile, direction='left'):
        full_img[0][c] = new_tiles[tile_key]
    elif match(np.fliplr(new_tiles[tile_key]), prev_tile, direction='left'):
        full_img[0][c] = np.fliplr(new_tiles[tile_key])

# top right corner
tile_key = str(int(full_tile_nums[0, -1]))
prev_tile = full_img[0][-2]
if match(new_tiles[tile_key], prev_tile, direction='left'):
    full_img[0][-1] = new_tiles[tile_key]
elif match(np.rot90(new_tiles[tile_key], 2).T, prev_tile, direction='left'):
    full_img[0][-1] = np.rot90(new_tiles[tile_key], 2).T

for r in range(1, row - 1):
    # right row
    tile_key = str(int(full_tile_nums[r, -1]))
    prev_tile = full_img[r - 1][-1]
    if match(new_tiles[tile_key], prev_tile, direction='top'):
        full_img[r][-1] = new_tiles[tile_key]
    elif match(np.flipud(new_tiles[tile_key]), prev_tile, direction='top'):
        full_img[r][-1] = np.flipud(new_tiles[tile_key])

# bottom right corner
tile_key = str(int(full_tile_nums[-1, -1]))
prev_tile = full_img[-2][-1]
if match(new_tiles[tile_key], prev_tile, direction='top'):
    full_img[-1][-1] = new_tiles[tile_key]
elif match(new_tiles[tile_key].T, prev_tile, direction='top'):
    full_img[-1][-1] = new_tiles[tile_key].T

for c in reversed(range(1, col - 1)):
    # bottom row
    tile_key = str(int(full_tile_nums[-1, c]))
    prev_tile = full_img[-1][c + 1]
    if match(new_tiles[tile_key], prev_tile, direction='right'):
        full_img[-1][c] = new_tiles[tile_key]
    elif match(np.fliplr(new_tiles[tile_key]), prev_tile, direction='right'):
        full_img[-1][c] = np.fliplr(new_tiles[tile_key])

# bottom left corner
tile_key = str(int(full_tile_nums[-1, 0]))
prev_tile = full_img[-1][1]
if match(new_tiles[tile_key], prev_tile, direction='right'):
    full_img[-1][0] = new_tiles[tile_key]
elif match(np.rot90(new_tiles[tile_key], 2).T, prev_tile, direction='right'):
    full_img[-1][0] = np.rot90(new_tiles[tile_key], 2).T

for r in reversed(range(1, row - 1)):
    # left row
    tile_key = str(int(full_tile_nums[r, 0]))
    prev_tile = full_img[r + 1][0]
    if match(new_tiles[tile_key], prev_tile, direction='bottom'):
        full_img[r][0] = new_tiles[tile_key]
    elif match(np.flipud(new_tiles[tile_key]), prev_tile, direction='bottom'):
        full_img[r][0] = np.flipud(new_tiles[tile_key])

print('filling in the other tile numbers...')
# fill in the other tile_nums
while list(full_tile_nums.reshape((-1))).count(0) != 0:
    for (r, c) in zip(np.where(full_tile_nums == 0)[0],
                      np.where(full_tile_nums == 0)[1]):

        for potential_tile, match_tiles in which_matches.items():

            if len(match_tiles) != 4:
                continue

            all_matches = []
            for key in directions.keys():

                dr, dc = [int(k) for k in key.split(',')]
                if 0 <= (r + dr) < row and 0 <= (c + dc) < col:
                    if full_tile_nums[r + dr, c + dc] == 0:
                        continue

                    if str(int(full_tile_nums[r + dr, c + dc])) in \
                            which_matches[str(potential_tile)]:
                        all_matches.append(True)
                    else:
                        all_matches.append(False)

            if all(all_matches) and len(all_matches) >= 2:

                if list(full_tile_nums.reshape((-1))).count(float(
                        potential_tile)) == 0:
                    full_tile_nums[r, c] = potential_tile
                    break

assert len(set(full_tile_nums.reshape((-1)))) == full_tile_nums.size

print('figuring out the orientation of the non-border tiles...')
# figure out the orientation of the rest of the non-border tiles
to_fill_idx = []
for r in range(row):
    for c in range(col):
        if full_img[r][c] is None:
            to_fill_idx.append([r, c])

while len(to_fill_idx) != 0:
    for cur_index, (r, c) in enumerate(to_fill_idx):

        tile_key = str(int(full_tile_nums[r, c]))
        cur_tile = new_tiles[tile_key]

        is_match = False
        for key, dir in directions.items():

            dr, dc = [int(k) for k in key.split(',')]
            if 0 <= (r + dr) < row and 0 <= (c + dc) < col and \
                    full_img[r + dr][c + dc] is not None:

                prev_key = str(int(full_tile_nums[r + dr, c + dc]))
                prev_tile = full_img[r + dr][c + dc]

                for i in range(4):
                    if match(np.rot90(cur_tile, i), prev_tile, direction=dir):
                        is_match = True
                        cur_tile = np.rot90(cur_tile, i)
                        break

                    elif match(np.rot90(cur_tile.T, i), prev_tile,
                               direction=dir):
                        is_match = True
                        cur_tile = np.rot90(cur_tile.T, i)
                        break

                if is_match:
                    break

        if is_match:
            full_img[r][c] = cur_tile
            to_fill_idx.pop(cur_index)
            print('.', end='')

# stitch together the image!
print('\nstitching together the image...')
for r in range(row):
    for c in range(col):
        full_img[r][c] = remove_border(full_img[r][c])

stacked_img = [np.concatenate(r, axis=-1) for r in full_img]
stacked_img = np.concatenate(stacked_img, axis=0)

print('finding the sea monster!')
sea_monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
sea_monster = sea_monster.strip('\n').replace(' ', '.')
sea_monster_row, sea_monster_col = 3, 20
stack_row, stack_col = stacked_img.shape
num_monsters, count = 0, 0

while num_monsters == 0:

    if count >= 4:
        copy_img = array_to_string(np.rot90(stacked_img, count))
    else:
        copy_img = array_to_string(np.rot90(stacked_img.T, count - 4))

    for r in range(stack_row):
        rstop = r + sea_monster_row
        if rstop > stack_row:
            break

        for c in range(stack_col):
            cstop = c + sea_monster_col
            if cstop > stack_col:
                break

            waters = '\n'.join([line[c:cstop] for line in copy_img[r:rstop]])
            if regex.fullmatch(sea_monster, waters):
                num_monsters += 1
                new_waters = ''.join(['o' if sm == '#' else w for w, sm in zip(
                    waters, sea_monster)])
                new_waters = new_waters.split('\n')
                for j, w in enumerate(new_waters):
                    this_line = list(copy_img[r + j])
                    this_line[c:cstop] = w
                    copy_img[r + j] = ''.join(this_line)
    count += 1

# determine water roughness
print('Part 2:', sum(r.count('#') for r in copy_img))
print(f'Runtime: {time.time() - part2_time:0.2f} s.')
