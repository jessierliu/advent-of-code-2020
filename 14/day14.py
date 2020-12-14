"""
Day 14
"""

import re
from itertools import product

with open('input.txt', 'r') as f:
    lines = f.read()

lines = lines.strip('\n').split('\n')


def new_mask(mask_line):
    m = {}
    for pos, char in enumerate(list(mask_line.strip('mask = '))):
        if char != 'X':
            m[pos] = char

    return m


def floating_mask(mask_line):
    m, f = [], []
    for pos, char in enumerate(list(mask_line.strip('mask = '))):
        if char == '1':
            m.append(pos)
        elif char == 'X':
            f.append(pos)

    return m, f


# part 1
memory, mask = {}, {}

for op in lines:

    if op[:4] == 'mask':
        mask = new_mask(op)

    else:
        value = int(op.replace(' ', '').split('=')[1])
        address = re.search(r'(?<=\[).+?(?=\])', op).group(0)
        value_bit = list(f'{value:036b}')

        for key, val in mask.items():
            value_bit[key] = val

        bit_value = sum([2 ** int(pos) for pos, val in enumerate(reversed(
            value_bit)) if val == '1'])

        memory[address] = bit_value

print(sum(memory.values()))

# part 2
memory, mask, float_pos = {}, {}, []

for op in lines:

    if op[:4] == 'mask':
        mask, float_pos = floating_mask(op)

    else:
        value = int(op.replace(' ', '').split('=')[1])
        address = re.search(r'(?<=\[).+?(?=\])', op).group(0)
        address_bit = list(f'{int(address):036b}')

        for key in mask:
            address_bit[key] = '1'

        bit_addresses = []
        for combo in product(['0', '1'], repeat=len(float_pos)):

            for key, val in zip(float_pos, combo):
                address_bit[key] = val

            bit_address = sum([2 ** int(pos) for pos, val in enumerate(
                reversed(address_bit)) if val == '1'])
            memory[bit_address] = value

print(sum(memory.values()))
