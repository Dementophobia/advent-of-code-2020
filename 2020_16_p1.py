from aoc import read_file, timer
from re import findall

@timer
def solve():
    mode, result, fields = 0, 0, set()
    
    for line in read_file("16"):
        if not len(line) or "ticket" in line:
            mode += 1
            continue
            
        if mode == 0:
            field = [int(num) for num in findall(r'\d+', line)]
            fields = fields | \
                     set(value for value in range(field[0], field[1] + 1)) | \
                     set(value for value in range(field[2], field[3] + 1))
                     
        if mode == 4:
            result += sum(int(value) for value in line.split(",") if int(value) not in fields)

    return result

result = solve()
print(f"Solution: {result}")