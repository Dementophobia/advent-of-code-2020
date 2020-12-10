from aoc import read_file, timer

@timer
def solve():
    adapters = sorted([int(line) for line in read_file("10")])
    adapters = [0] + adapters + [adapters[-1] + 3]

    diffs = [adapters[index + 1] - adapters[index] for index in range(len(adapters) - 1)]
    
    return diffs.count(1) * diffs.count(3)

result = solve()
print(f"Solution: {result}")