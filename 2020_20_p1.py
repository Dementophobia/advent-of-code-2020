from aoc import read_file, timer
from re import findall
from collections import defaultdict

def get_borders(raw_input):
    tiles = defaultdict(list)
    for line in raw_input:
        if not len(line):
            continue
        elif (tile := findall(r"(\d+)", line)):
            tile_id = tile[0]
        else:
            tiles[tile_id].append([pixel == "#" for pixel in line])
    
    borders = defaultdict(list)
    
    for tile, pixels in tiles.items():
        borders_pixels = ["".join(["1" if pixel else "0" for pixel in pixels[0]]),
                          "".join(["1" if pixel else "0" for pixel in [p[0] for p in pixels]][::-1]),
                          "".join(["1" if pixel else "0" for pixel in pixels[9]][::-1]),
                          "".join(["1" if pixel else "0" for pixel in [p[9] for p in pixels]])]

        borders[tile] = [int(borders_pixels[i][::direction], 2) for i in range(4) for direction in (-1, 1)]

    return borders

@timer
def solve():
    raw_input = read_file("20")
    tile_borders = get_borders(raw_input)
    
    result = 1
    
    for tile, borders in tile_borders.items():
        neighbors = set()
        for other_tile, other_borders in tile_borders.items():
            if tile == other_tile:
                continue
            
            for border in borders:
                if border in other_borders:
                    neighbors.add(other_tile)

        if len(neighbors) == 2:
            result *= int(tile)

    return result

result = solve()
print(f"Solution: {result}")