"""
Day 12
"""

with open('input.txt', 'r') as f:
    lines = f.read()
    lines = lines.strip('\n').split('\n')

pos = [0, 0]
angle = 90

for line in lines:
    if line[0] == 'F':
        if angle == 0:
            pos[1] += int(line[1:])
        elif angle == 90:
            pos[0] += int(line[1:])
        elif angle == 180:
            pos[1] -= int(line[1:])
        elif angle == 270:
            pos[0] -= int(line[1:])

    elif line[0] == 'N':
        pos[1] += int(line[1:])

    elif line[0] == 'S':
        pos[1] -= int(line[1:])

    elif line[0] == 'E':
        pos[0] += int(line[1:])

    elif line[0] == 'W':
        pos[0] -= int(line[1:])

    elif line[0] == 'R':
        angle += int(line[1:])

    elif line[0] == 'L':
        angle -= int(line[1:])

    angle = angle % 360

print(sum(map(abs, pos)))

# part 2
wx, wy = 10, 1
px, py = 0, 0

for line in lines:

    if line[0] == 'F':
        px += int(line[1:]) * wx
        py += int(line[1:]) * wy

    elif line[0] == 'N':
        wy += int(line[1:])

    elif line[0] == 'S':
        wy -= int(line[1:])

    elif line[0] == 'E':
        wx += int(line[1:])

    elif line[0] == 'W':
        wx -= int(line[1:])

    elif line[0] in ['L', 'R']:

        if line in ['L90', 'R270']:
            wx, wy = -wy, wx
        elif line in ['L180', 'R180']:
            wx, wy = -wx, -wy
        elif line in ['L270', 'R90']:
            wx, wy = wy, -wx

print(abs(px) + abs(py))
