from aoc import read_file, timer
from collections import defaultdict

def get_visible_seats(layout):
    visible_seats = defaultdict(list)

    for x, y in (area := layout.keys()):
        for dir in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            x_ray, y_ray = x, y
            while ((x_ray := x_ray + dir[0]), (y_ray := y_ray + dir[1])) in area:
                if layout[(x_ray, y_ray)] != ".":
                    visible_seats[(x, y)].append((x_ray, y_ray))
                    break

    return visible_seats

def change_seat(x, y, layout, visible_seats):
    if layout[(x, y)] == ".":
        return "."
    
    elif layout[(x, y)] == "L":
        if not sum([layout[pos] == "#" for pos in visible_seats[(x, y)]]):
            return "#"
        return "L"
    
    elif layout[(x, y)] == "#":
        if sum([layout[pos] == "#" for pos in visible_seats[(x, y)]]) >= 5:
            return "L"
        return "#"

def next_round(layout, visible_seats):
    next_layout = defaultdict(str)
    for pos, value in list(layout.items()):
        next_layout[pos] = change_seat(*pos, layout, visible_seats)
    return next_layout

@timer
def solve():
    raw_input = read_file("11")
    layout = defaultdict(str)
    
    for y in range(len(raw_input)):
        for x in range(len(raw_input[0])):
            layout[(x, y)] = raw_input[y][x]
    
    visible_seats = get_visible_seats(layout)

    last_seen = defaultdict(str)
    while (layout := next_round(layout, visible_seats)) != last_seen:
        last_seen = layout
    
    return sum([seat == "#" for seat in layout.values()])

result = solve()
print(f"Solution: {result}")