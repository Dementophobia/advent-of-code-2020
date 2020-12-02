from aoc import read_file, timer

@timer
def solve():
    input = read_file("01")
    input = sorted([int(line) for line in input])

    for a in range(len(input)):
        for b in range(a+1, len(input)-1):
            if input[a] + input[b] > 2020:
                break
            for c in range(b+1, len(input)-2):
                if input[a] + input[b] + input[c] > 2020:
                    break
                elif input[a] + input[b] + input[c] == 2020:
                    return input[a] * input[b] * input[c]

result = solve()
print(f"Solution: {result}")