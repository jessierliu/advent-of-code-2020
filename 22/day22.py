"""
Day 22
"""


def get_fresh_cards():
    with open('input.txt', 'r') as f:
        lines = f.read()
    p1, p2 = lines.split('\n\n')
    p1 = p1.replace('Player 1:', '').strip('\n').split('\n')
    p2 = p2.replace('Player 2:', '').strip('\n').split('\n')
    return [int(p) for p in p1], [int(p) for p in p2]


# part 1
p1, p2 = get_fresh_cards()

while len(p1) != 0 and len(p2) != 0:

    # draw a card
    card1, card2 = p1.pop(0), p2.pop(0)

    if card1 > card2:
        p1.extend([card1, card2])
    else:
        p2.extend([card2, card1])

if len(p1) != 0:
    print('Player 1 wins!')
    card_tally = [c * (i + 1) for c, i in zip(p1, reversed(range(len(p1))))]
    print(sum(card_tally))
elif len(p2) != 0:
    print('Player 2 wins!')
    card_tally = [c * (i + 1) for c, i in zip(p2, reversed(range(len(p2))))]
    print(sum(card_tally))


# part 2
def join_list(one, two):
    one = '_'.join([str(o) for o in one])
    two = '_'.join([str(t) for t in two])
    return one + '-' + two


def sub_game(cards1, cards2, default_p1=False):
    past = []

    while len(cards1) != 0 and len(cards2) != 0:

        new_key = join_list(cards1, cards2)
        if new_key in past:
            default_p1 = True
            break
        else:
            past.append(new_key)

        # draw a card
        c1, c2 = cards1.pop(0), cards2.pop(0)

        if len(cards1) >= c1 and len(cards2) >= c2:
            # trigger subgame
            new_cards1 = cards1.copy()
            new_cards2 = cards2.copy()
            winner, _, _ = sub_game(new_cards1[:c1], new_cards2[:c2])

        else:
            if c1 > c2:
                winner = 'player1'
            else:
                winner = 'player2'

        if winner == 'player1':
            cards1.extend([c1, c2])
        elif winner == 'player2':
            cards2.extend([c2, c1])

    if len(cards1) != 0 or default_p1:
        return 'player1', cards1, cards2
    else:
        return 'player2', cards1, cards2


p1, p2 = get_fresh_cards()
win, p1, p2 = sub_game(p1, p2)
if len(p1) != 0:
    print('Player 1 wins!')
    card_tally = [c * (i + 1) for c, i in zip(p1, reversed(range(len(p1))))]
    print(sum(card_tally))
elif len(p2) != 0:
    print('Player 2 wins!')
    card_tally = [c * (i + 1) for c, i in zip(p2, reversed(range(len(p2))))]
    print(sum(card_tally))
