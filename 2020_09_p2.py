from aoc import read_file, timer

def is_valid(preamble, val):
    for a in range(25):
        for b in range(a+1, len(preamble)):
            if preamble[a] + preamble[b] == val:
                return True
    return False

@timer
def solve():
    code = [int(line) for line in read_file("09")]
    
    for start in range(25, len(code)):
        if not is_valid(code[start-25:start], code[start]):
            value = code[start]
            break
    
    for start in range(len(code)):
        running_sum = 0
        for length in range(len(code)-start):
            if (running_sum := running_sum + code[start+length]) > value:
                break
            elif running_sum == value:
                return min(code[start:start+length]) + max(code[start:start+length])

result = solve()
print(f"Solution: {result}")