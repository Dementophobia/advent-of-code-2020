from aoc import read_file, timer

@timer
def solve():
    input = read_file("03")
    x_pos  = -3
    return sum([line[(x_pos := (x_pos + 3) % len(input[0]))] == "#" for line in input])

result = solve()
print(f"Solution: {result}")