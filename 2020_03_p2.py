from aoc import read_file, timer

@timer
def solve():
    input = read_file("03")
    trees = 1
    
    for slope in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
        x_pos  = -slope[1]
        trees *= sum([input[line_index][(x_pos := (x_pos + slope[1]) % len(input[0]))] == "#" for line_index in range(0, len(input), slope[0])])
    
    return trees

result = solve()
print(f"Solution: {result}")

