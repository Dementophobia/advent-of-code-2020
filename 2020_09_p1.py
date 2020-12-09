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
    
    for index in range(25, len(code)):
        if not is_valid(code[index-25:index], code[index]):
            return code[index]

result = solve()
print(f"Solution: {result}")