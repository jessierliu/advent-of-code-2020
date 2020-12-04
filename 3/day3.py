"""
Day 3
"""

def check_trees(given_slope=None, forest=None):

    cur_line, cur_pos = given_slope
    trees = 0

    while cur_line < len(forest):

        if forest[cur_line][cur_pos] == '#':
            trees += 1

        cur_line += given_slope[0]
        cur_pos += given_slope[1]

    return trees


with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.split('\n')[:-1]
lines = [l*len(lines) for l in lines]

print(check_trees(given_slope=[1, 3], forest=lines))

all_trees = 1
slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
for slope in slopes:
    all_trees *= check_trees(given_slope=slope, forest=lines)

print(all_trees)
