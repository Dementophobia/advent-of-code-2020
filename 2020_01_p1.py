from aoc import read_file, timer

@timer
def solve():
    input = read_file("01")
    input = sorted([int(line) for line in input])
    
    for a in range(len(input)):
        for b in range(len(input)-1, a+1, -1):
            if input[a] + input[b] < 2020:
                break
            elif input[a] + input[b] == 2020:
                return input[a] * input[b]

result = solve()
print(f"Solution: {result}")