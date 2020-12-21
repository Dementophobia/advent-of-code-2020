from aoc import read_file, timer
from re import findall
from collections import defaultdict

def build_tiles(raw_input):
    tiles_pixels = defaultdict(list)
    for line in raw_input:
        if not len(line):
            continue
        elif (tile := findall(r"(\d+)", line)):
            tile_id = tile[0]
        else:
            tiles_pixels[tile_id].append([pixel == "#" for pixel in line])
    
    borders = defaultdict(list)
    
    for tile, pixels in tiles_pixels.items():
        borders_pixels = ["".join(["1" if pixel else "0" for pixel in pixels[0]]),
                          "".join(["1" if pixel else "0" for pixel in [p[0] for p in pixels]][::-1]),
                          "".join(["1" if pixel else "0" for pixel in pixels[9]][::-1]),
                          "".join(["1" if pixel else "0" for pixel in [p[9] for p in pixels]])]

        borders[tile].append([int(borders_pixels[i], 2) for i in range(4)])
        borders[tile].append([int(borders_pixels[i][::-1], 2) for i in range(4)]) 

        borders[tile][1][0], borders[tile][1][2] = borders[tile][1][2], borders[tile][1][0]
        
        for rotation in range(3):
            for side in range(2):
                borders[tile].append(borders[tile][side + 2 * rotation][1:] + \
                                    [borders[tile][side + 2 * rotation][0]])
        
    return tiles_pixels, borders

def transform(tile, orientation, tiles_pixels, tiles_borders):
    tiles_pixels[tile] = tiles_pixels[tile][1:-1]
    tiles_pixels[tile] = [tiles_pixels[tile][y][1:-1] for y in range(len(tiles_pixels[tile]))]

    tiles_borders[tile] = tiles_borders[tile][orientation]

    if orientation % 2:
        tiles_pixels[tile] = tiles_pixels[tile][::-1]
    
    for rotation in range(orientation // 2):
        tiles_pixels[tile] = [[tiles_pixels[tile][x][y] for x in range(len(tiles_pixels[tile][y]))][::-1]
                              for y in range(len(tiles_pixels[tile]))]

def find_top_left(puzzle, tiles_borders, tiles_neighbors, tiles_pixels):
    for tile, borders in tiles_borders.items():
        for other_tile, other_border in tiles_borders.items():
            if tile == other_tile:
                continue
            
            for border_variation in [borders[0]]:
                for border in border_variation:
                    if border in (b for b_var in other_border for b in b_var):
                        tiles_neighbors[tile].add((other_tile, border, int(f"{border:08b}"[::-1], 2)))

    for tile, neighbors in tiles_neighbors.items():
        if len(neighbors) == 2:
            puzzle[(0,0)] = tile
            break

    for orientation in range(8):
        if sum([neighbor[1] in [tiles_borders[tile][orientation][side] for side in (2, 3)]
                                for neighbor in tiles_neighbors[tile]]) == 2:
            break

    transform(tile, orientation, tiles_pixels, tiles_borders)

def find_top_row(puzzle, puzzle_size, tiles_borders, tiles_pixels):
    for position in range(1, puzzle_size):
        next_border = int(f"{tiles_borders[puzzle[(position - 1, 0)]][3]:010b}"[::-1], 2)
        for tile in tiles_pixels.keys():
            if tile in puzzle.values():
                continue
            for orientation in range(8):
                if next_border == tiles_borders[tile][orientation][1]:
                    break
            else:
                continue
            break
        
        transform(tile, orientation, tiles_pixels, tiles_borders)
        puzzle[(position, 0)] = tile

def find_remaining_rows(puzzle, puzzle_size, tiles_borders, tiles_pixels):
    for position_y in range(1, puzzle_size):
        for position_x in range(puzzle_size):
            next_border = int(f"{tiles_borders[puzzle[(position_x, position_y - 1)]][2]:010b}"[::-1], 2)
            for tile in tiles_pixels.keys():
                if tile in puzzle.values():
                    continue
                for orientation in range(8):
                    if next_border == tiles_borders[tile][orientation][0]:
                        break
                else:
                    continue
                break
        
            transform(tile, orientation, tiles_pixels, tiles_borders)
            puzzle[(position_x, position_y)] = tile

def assemble_puzzle(puzzle, puzzle_size, tiles_pixels):
    full_puzzle = []
    
    for piece_y in range(puzzle_size):
        for row in range(len(tiles_pixels[puzzle[(0, piece_y)]])):
            full_row = []
            for piece_x in range(puzzle_size):
                full_row.extend(["#" if value else " " for value in tiles_pixels[puzzle[(piece_x, piece_y)]][row]])
            full_puzzle.append(full_row)
    
    return full_puzzle

def find_dragon(full_puzzle):
    dragon = ["                  # ",
              "#    ##    ##    ###",
              " #  #  #  #  #  #   "]
    dragon_offsets = [(x, y) for x in range(len(dragon[0])) 
                             for y in range(len(dragon))
                             if dragon[y][x] == "#"]
    found = False
    
    for flip in range(2):
        for rotation in range(3):
            for y in range(len(full_puzzle) - len(dragon)):
                for x in range(len(full_puzzle[0]) - len(dragon[0])):
                    for x_dragon, y_dragon in dragon_offsets:
                        if not full_puzzle[y + y_dragon][x + x_dragon] == "#":
                            break
                    else:
                        found = True
                        for x_dragon, y_dragon in dragon_offsets:
                            full_puzzle[y + y_dragon][x + x_dragon] = "O"
        
            if found:
                return sum([line.count("#") for line in full_puzzle])
            
            full_puzzle = [[full_puzzle[x][y] for x in range(len(full_puzzle[y]))][::-1]
                                              for y in range(len(full_puzzle))]
        full_puzzle = full_puzzle[::-1]

@timer
def solve():
    raw_input = read_file("20")
    tiles_pixels, tiles_borders = build_tiles(raw_input)
    tiles_neighbors, puzzle = defaultdict(set), defaultdict(str)
    puzzle_size = int(len(tiles_pixels)**0.5)
    
    find_top_left(puzzle, tiles_borders, tiles_neighbors, tiles_pixels)
    find_top_row(puzzle, puzzle_size, tiles_borders, tiles_pixels)
    find_remaining_rows(puzzle, puzzle_size, tiles_borders, tiles_pixels)
    full_puzzle = assemble_puzzle(puzzle, puzzle_size, tiles_pixels)
    
    return find_dragon(full_puzzle) 

result = solve()
print(f"Solution: {result}")