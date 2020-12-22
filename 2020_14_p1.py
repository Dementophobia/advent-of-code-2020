from aoc import read_file, timer
from re import match

@timer
def solve():
    raw_input = read_file("14")
    memory = dict()
    
    for line in raw_input:
        if mask_match := match(r"mask = ([X01]+)", line):
            mask = mask_match.group(1)
        else:
            address, value = match(r"mem\[(\d+)\] = (\d+)", line).group(1, 2)
            value = list(f'{int(value):036b}')
            value = [value[i] if mask[i] == "X" else mask[i] for i in range(36)]
            memory[address] = int("".join(value), 2)
    
    return sum([value for value in memory.values()])

result = solve()
print(f"Solution: {result}")