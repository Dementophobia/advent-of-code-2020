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

def play(decks):
    known = set()
    while len(decks[0]) and len(decks[1]):
        if (state := tuple(decks[0])) in known:
            return 0, None
        known.add(state)
        
        card_0, card_1 = decks[0].popleft(), decks[1].popleft()
        
        if len(decks[0]) < card_0 or len(decks[1]) < card_1:
            if card_0 > card_1:
                decks[0].extend([card_0, card_1])
            else:
                decks[1].extend([card_1, card_0])
        else:
            if not play([deque(list(decks[0])[:card_0]), deque(list(decks[1])[:card_1])])[0]:
                decks[0].extend([card_0, card_1])
            else:
                decks[1].extend([card_1, card_0])

    return min(len(decks[1]), 1), decks

@timer
def solve():
    winner, decks = play(build_decks(read_file("22")))
    return sum([decks[winner].pop() * multiplier for multiplier in range(1, len(decks[winner]) + 1)])

result = solve()
print(f"Solution: {result}")