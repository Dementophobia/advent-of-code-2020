from aoc import read_file, timer
from collections import defaultdict

def change_seat(x, y, layout):
    if layout[(x, y)] == ".":
        return "."
    
    elif layout[(x, y)] == "L":
        if not sum([layout[pos] == "#"
                           for x_offset in [-1, 0, 1]
                           for y_offset in [-1, 0, 1]
                           if (pos := (x + x_offset, y + y_offset)) in layout.keys()]):
            return "#"
        return "L"
    
    elif layout[(x, y)] == "#":
        if sum([layout[pos] == "#"
                       for x_offset in [-1, 0, 1]
                       for y_offset in [-1, 0, 1]
                       if (pos := (x + x_offset, y + y_offset)) in layout.keys()]) >= 5:
            return "L"
        return "#"

def next_round(layout):
    next_layout = defaultdict(str)
    for pos, value in list(layout.items()):
        next_layout[pos] = change_seat(*pos, layout)
    return next_layout

@timer
def solve():
    raw_input = read_file("11")
    layout = defaultdict(str)
    
    for y in range(len(raw_input)):
        for x in range(len(raw_input[0])):
            layout[(x, y)] = raw_input[y][x]
    
    last_seen = defaultdict(str)
    while (layout := next_round(layout)) != last_seen:
        last_seen = layout
    
    return sum([seat == "#" for seat in layout.values()])

result = solve()
print(f"Solution: {result}")