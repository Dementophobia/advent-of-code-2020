from aoc import read_file, timer

@timer
def solve():
    code = [line.split() for line in read_file("08")]
    accu, pos = 0, 0
    seen = set()
    
    while pos not in seen:
        seen.add(pos)
        
        if code[pos][0] == "acc":
            accu += int(code[pos][1])
        elif code[pos][0] == "jmp":
            pos += int(code[pos][1]) - 1
        
        pos += 1
    
    return accu

result = solve()
print(f"Solution: {result}")