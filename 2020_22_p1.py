from aoc import read_file, timer
from collections import deque

def build_decks(raw_input):
    player, decks = 0, [deque(), deque()]
    for line in raw_input:
        if not len(line):
            player = 1
            continue
        if "Player" not in line:
            decks[player].append(int(line))
    
    return decks
    
@timer
def solve():
    decks = build_decks(read_file("22"))

    while len(decks[0]) and len(decks[1]):
        card_0, card_1 = decks[0].popleft(), decks[1].popleft()
        if card_0 > card_1:
            decks[0].extend([card_0, card_1])
        else:
            decks[1].extend([card_1, card_0])

    winning_deck = sorted(decks, key = lambda deck: len(deck))[1]
    return sum([winning_deck.pop() * multiplier for multiplier in range(1, len(winning_deck) + 1)])

result = solve()
print(f"Solution: {result}")