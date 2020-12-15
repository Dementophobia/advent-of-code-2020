from aoc import read_file, timer
from collections import defaultdict

@timer
def solve():
    numbers = [int(number) for number in read_file("15")[0].split(",")]
    seen = defaultdict(list, {numbers[i]: [i] for i in range(len(numbers))})    
    counter, current = len(numbers) - 1, numbers[-1]

    while (counter := counter + 1) < 30000000:
        if len(seen[current]) == 1:
            seen[(current := 0)].append(counter)
        else:
            seen[(current := seen[current][-1] - seen[current][-2])].append(counter)

    return current

result = solve()
print(f"Solution: {result}")