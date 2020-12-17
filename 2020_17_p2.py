from aoc import read_file, timer
from collections import defaultdict

def next_state(x, y, z, w, grid):
    neighbors = [(x + x_dir, y + y_dir, z + z_dir, w + w_dir)
                 for x_dir in (-1, 0, 1)
                 for y_dir in (-1, 0, 1)
                 for z_dir in (-1, 0, 1)
                 for w_dir in (-1, 0, 1)
                 if x_dir or y_dir or z_dir or w_dir]
    
    amount_of_neighors = sum([grid[neighbor] for neighbor in neighbors])
    
    if grid[(x, y, z, w)]:
        if (amount_of_neighors == 2 or amount_of_neighors == 3):
            return True
        return False
    
    if amount_of_neighors == 3:
        return True
    return False

def cycle(boundary, grid):
    for parameter in ("x_max", "y_max", "z_max", "w_max"):
        boundary[parameter] += 1
    for parameter in ("x_min", "y_min", "z_min", "w_min"):
        boundary[parameter] -= 1
    
    return defaultdict(bool, {(x, y, z, w): next_state(x, y, z, w, grid)
                              for w in range(boundary["w_min"], boundary["w_max"])
                              for z in range(boundary["z_min"], boundary["z_max"])
                              for y in range(boundary["y_min"], boundary["y_max"])
                              for x in range(boundary["x_min"], boundary["x_max"])})
   
@timer
def solve():
    raw_input = read_file("17")
    boundary = {"x_max": len(raw_input[0]), "y_max": len(raw_input), "z_max": 1, "w_max": 1,
                "x_min": 0, "y_min": 0, "z_min": 0, "w_min": 0}
    grid = defaultdict(bool, {(x, y, 0, 0): raw_input[y][x] == "#"
                              for y in range(boundary["y_max"])
                              for x in range(boundary["x_max"])})

    for _ in range(6):
        grid = cycle(boundary, grid)
   
    return sum(grid.values())

result = solve()
print(f"Solution: {result}")