"""
Day 25
"""


def get_loop_size(num, key, value=1, loop=True):
    counter = 0
    while loop:
        value *= num
        value = value % 20201227
        counter += 1
        if value == key:
            loop = False
    return counter


def transform(num, loop_size, value=1):
    for _ in range(loop_size):
        value *= num
        value = value % 20201227
    return value


with open('input.txt', 'r') as f:
    card_key, door_key = [int(i) for i in f.read().strip('\n').split('\n')]

card_loop_size = get_loop_size(7, card_key)
door_loop_size = get_loop_size(7, door_key)
encryption_key = transform(door_key, card_loop_size)
print('Part 1:', encryption_key)
