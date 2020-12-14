from aoc import read_file, timer

@timer
def solve():
    raw_input = read_file("14")
    memory = dict()
    
    for line in raw_input:
        if line[:4] == "mask":
            mask = line.split(" = ")[1]
        else:
            addr = line.split("]")[0][4:]
            value = list(f'{int(line.split(" = ")[1]):036b}')
            
            for i in range(36):
                if mask[i] == "X":
                    continue
                value[i] = mask[i]
            
            memory[addr] = int("".join(value), 2)
    
    return sum([value for value in memory.values()])

result = solve()
print(f"Solution: {result}")