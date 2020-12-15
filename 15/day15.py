"""
Day 15
"""

input_sequence = [0, 13, 16, 17, 1, 10, 6]


def get_last_turn(starter, last_turn):
    turns = {}
    for val, key in enumerate(starter[:-1]):
        turns[key] = val

    prev_turn = starter[-1]
    for i in range(len(starter) - 1, last_turn - 1):

        try:
            cur_turn = i - turns[prev_turn]

        except KeyError:
            cur_turn = 0

        turns[prev_turn] = i
        prev_turn = cur_turn

    print(prev_turn)


# part 1
get_last_turn(input_sequence, 2020)

# part 2
get_last_turn(input_sequence, 30000000)
