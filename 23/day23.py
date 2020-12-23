"""
Day 23
"""


def play_game(pcups, num_cups=None, rounds=None):
    max_cups = max(pcups)
    cur_cup = pcups[0]
    cups = {}

    if num_cups is not None:
        for cur, next in zip(pcups, pcups[1:] + [max_cups + 1]):
            cups[cur] = next

        for cur, next in zip(range(max_cups + 1, int(1e6) + 1),
                             list(range(max_cups + 2, int(1e6) + 1)) + [
                                 cur_cup]):
            cups[cur] = next

        max_cups = num_cups

    else:
        for cur, next in zip(pcups, pcups[1:] + [pcups[0]]):
            cups[cur] = next

    for _ in range(int(rounds)):

        # pick up next 3 cups
        pickup1 = cups[cur_cup]
        pickup2 = cups[pickup1]
        pickup3 = cups[pickup2]

        # move up the cups
        cups[cur_cup] = cups[pickup3]

        # destination cup
        dest_cup = cur_cup
        while dest_cup in [cur_cup, pickup1, pickup2, pickup3]:
            dest_cup -= 1
            if dest_cup == 0:
                dest_cup = int(max_cups)

        # destination location
        # pickup 1 is now next after the destination cup
        # cup after pickup 1 is still pickup 2
        # cup after pickup 2 is still pickup 3
        # cup after pickup 3 is now the cup after the destination cup
        past_dest_cup = cups[dest_cup]
        cups[dest_cup] = pickup1
        cups[pickup3] = past_dest_cup

        # next current cup
        cur_cup = cups[cur_cup]

    return cups


play_cups = [int(c) for c in '624397158']

new_cups = play_game(play_cups, rounds=100)
last_label = str(new_cups[1])
for _ in range(len(play_cups) - 2):
    last_label += str(new_cups[int(last_label[-1])])
print('Part 1:', last_label)

new_cups = play_game(play_cups, rounds=1e7, num_cups=1e6)
print('Part 2:', new_cups[1] * new_cups[new_cups[1]])
