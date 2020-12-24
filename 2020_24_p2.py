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

def pass_day(this_day):
    for tile in list(this_day.keys()):
        if this_day[tile] == 0:
            for neighbor in [( 1, 0), (0,  1), ( 1,  1),
                             (-1, 0), (0, -1), (-1, -1)]:
                this_day[(tile[0] + neighbor[0], tile[1] + neighbor[1])]

    next_day = this_day.copy()

    for tile in list(this_day.keys()):
        black_neighbors = sum([this_day[(tile[0] + neighbor[0],
                                         tile[1] + neighbor[1])] == 0
                               for neighbor in [( 1, 0), (0,  1), ( 1,  1),
                                                (-1, 0), (0, -1), (-1, -1)]])

        if this_day[tile] == 0 and (not black_neighbors or black_neighbors > 2):
            next_day[tile] = 1
        elif this_day[tile] == 1 and black_neighbors == 2:
            next_day[tile] = 0

    return next_day

@timer
def solve():
    raw_input = read_file("24")
    color_of_tiles = defaultdict(lambda: 1)
    
    for instruction in raw_input:
        location = normalize(instruction)
        color_of_tiles[location] = (color_of_tiles[location] + 1) % 2
    
    for _ in range(100):
        color_of_tiles = pass_day(color_of_tiles)
    
    return (sum([color == 0 for color in color_of_tiles.values()]))

result = solve()
print(f"Solution: {result}")