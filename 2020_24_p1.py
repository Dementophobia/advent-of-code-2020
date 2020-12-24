from aoc import read_file, timer
from collections import defaultdict
from re import sub

def normalize(instruction):
    directions = defaultdict(int)
    for direction_pair in [("se", "nw"), ("sw", "ne"), ("e", "w")]:
        directions[direction_pair[0]] = \
        instruction.count(direction_pair[0]) - instruction.count(direction_pair[1])

        for direction in direction_pair:
            instruction = sub(direction, "", instruction)
    
    return tuple((directions["sw"] + directions["se"], directions["e"]  + directions["se"]))

@timer
def solve():
    raw_input = read_file("24")
    flips_per_tile = defaultdict(int)
    
    for instruction in raw_input:
        flips_per_tile[normalize(instruction)] += 1
        
    return sum([flips % 2 for flips in flips_per_tile.values()])

result = solve()
print(f"Solution: {result}")