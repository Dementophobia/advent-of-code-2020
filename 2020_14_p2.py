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
            addresses, value = match(r"mem\[(\d+)\] = (\d+)", line).group(1, 2)
            addresses = list(f'{int(addresses):036b}')
            addresses = [["1" if mask[i] == "1" else addresses[i] for i in range(36)]]
            
            for i in range(36):
                if mask[i] == "X":
                    addresses = [address[:i] + [bit] + address[i+1:] for bit in ("0", "1") for address in addresses]
            
            for address in addresses:
                memory[tuple(address)] = int(value)
    
    return sum((value for value in memory.values()))

result = solve()
print(f"Solution: {result}")