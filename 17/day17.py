"""
Day 17
"""

from itertools import product

with open('input.txt', 'r') as f:
    lines = f.read()
    lines = [list(l) for l in lines.strip('\n').split('\n')]


def total_active(data):
    total_active = 0
    for z, value in data.items():
        for x, val in value.items():
            for y, state in val.items():
                if state == '#':
                    total_active += 1
    return total_active


def apply_update(data, new):
    for (z, x, y), val in new.items():
        if z not in data.keys():
            data[z] = {}
        if x not in data[z].keys():
            data[z][x] = {}
        data[z][x][y] = val
    return data


# (z, x, y)
pocket = {0: {}}
for x, line in enumerate(lines):
    pocket[0][x] = {}
    for y, val in enumerate(line):
        pocket[0][x][y] = val

for cur_cycle in range(6):

    to_update = {}
    for z, value in pocket.items():
        for x, val in value.items():
            for y, state in val.items():
                for nx, ny, nz in product([0, 1, -1], repeat=3):
                    try:
                        test = pocket[z + nz][x + nx][y + ny]
                    except KeyError:
                        # not logged yet, all start inactive
                        to_update[(z + nz, x + nx, y + ny)] = '.'

    # apply update
    pocket = apply_update(pocket, to_update)

    for z, value in pocket.items():
        for x, val in value.items():
            for y, state in val.items():
                # check neighbors
                nb_active = 0
                for nx, ny, nz in product([0, 1, -1], repeat=3):
                    if [nx, ny, nz] == [0, 0, 0]:
                        continue

                    try:
                        if pocket[z + nz][x + nx][y + ny] == '#':
                            nb_active += 1
                    except KeyError:
                        pass

                if state == '#' and nb_active in [2, 3]:
                    pass
                else:
                    to_update[(z, x, y)] = '.'

                if state == '.' and nb_active == 3:
                    to_update[(z, x, y)] = '#'
                else:
                    pass

    # apply update
    pocket = apply_update(pocket, to_update)

print(total_active(pocket))


# part 2: 4 dimensions
def total_active4(data):
    total_active = 0
    for z, value in data.items():
        for x, val in value.items():
            for y, va in val.items():
                for w, state in va.items():
                    if state == '#':
                        total_active += 1
    return total_active


def apply_update4(data, new):
    for (z, x, y, w), val in new.items():
        if z not in data.keys():
            data[z] = {}
        if x not in data[z].keys():
            data[z][x] = {}
        if y not in data[z][x].keys():
            data[z][x][y] = {}
        data[z][x][y][w] = val
    return data


pocket = {0: {}}
for x, line in enumerate(lines):
    pocket[0][x] = {}
    for y, val in enumerate(line):
        pocket[0][x][y] = {0: val}

for cur_cycle in range(6):

    to_update = {}
    for z, value in pocket.items():
        for x, val in value.items():
            for y, va in val.items():
                for w, state in va.items():
                    for nx, ny, nz, nw in product([0, 1, -1], repeat=4):
                        try:
                            test = pocket[z + nz][x + nx][y + ny][w + nw]
                        except KeyError:
                            # not logged yet, all start inactive
                            to_update[(z + nz, x + nx, y + ny, w + nw)] = '.'

    # apply update
    pocket = apply_update4(pocket, to_update)

    for z, value in pocket.items():
        for x, val in value.items():
            for y, va in val.items():
                for w, state in va.items():
                    # check neighbors
                    nb_active = 0
                    for nx, ny, nz, nw in product([0, 1, -1], repeat=4):
                        if [nx, ny, nz, nw] == [0, 0, 0, 0]:
                            continue

                        try:
                            if pocket[z + nz][x + nx][y + ny][w + nw] == '#':
                                nb_active += 1
                        except KeyError:
                            pass

                    if state == '#' and nb_active in [2, 3]:
                        pass
                    else:
                        to_update[(z, x, y, w)] = '.'

                    if state == '.' and nb_active == 3:
                        to_update[(z, x, y, w)] = '#'
                    else:
                        pass

    # apply update
    pocket = apply_update4(pocket, to_update)

print(total_active4(pocket))
