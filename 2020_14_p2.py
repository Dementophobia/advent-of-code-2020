from aoc import read_file, timer

@timer
def solve():
    raw_input = read_file("14")
    memory = dict()
    
    for line in raw_input:
        if line[:4] == "mask":
            mask = line.split(" = ")[1]
        else:
            addr = list(f'{int(line.split("]")[0][4:]):036b}')
            value = int(line.split(" = ")[1])
            
            for i in range(36):
                if mask[i] == "1":
                    addr[i] = "1"
            
            addresses = [addr]
            
            for i in range(36):
                if mask[i] == "X":
                    new_addresses = []
                    for address in addresses:
                        address = address[:i] + ["0"] + address[i+1:]
                        new_addresses.append(address)
                        address = address[:i] + ["1"] + address[i+1:]
                        new_addresses.append(address)
                    addresses = new_addresses
            
            for address in addresses:
                memory[int("".join(address), 2)] = value
    
    return sum([value for value in memory.values()])

result = solve()
print(f"Solution: {result}")