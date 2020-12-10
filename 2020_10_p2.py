from aoc import read_file, timer
from functools import reduce

def analyze_sequences(adapters):
    sequences = [1]

    for index in range(len(adapters)-1):
        if adapters[index + 1] - adapters[index] == 1:
            sequences[-1] += 1
        elif adapters[index + 1] - adapters[index] == 3:
            sequences.append(1)
    
    return sequences

@timer
def solve():
    adapters = sorted([int(line) for line in read_file("10")])
    adapters = [0] + adapters + [adapters[-1] + 3]

    return reduce(lambda a, b: a * b, [[1, 2, 4, 7][max(0, s - 2)] for s in analyze_sequences(adapters)])

result = solve()
print(f"Solution: {result}")