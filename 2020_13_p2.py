from aoc import read_file, timer
from functools import reduce
from re import findall

def find_values(offset, increment, ids, pos, index):
    result, i = [], 0
    
    while len(result) < 2:
        if not (offset + i * increment + pos[index]) % ids[index]:
            result.append(offset + i * increment)
        i += 1

    return result[0], result[1] - result[0]

@timer
def solve():
    raw_input = read_file("13")
    ids = findall(r'\d+', raw_input[1])
    all_entries = raw_input[1].split(",")
    pos = [all_entries.index(id) for id in ids]
    ids = [int(id) for id in ids]
    
    offset, increment = 0, 1
    for i in range (len(ids)):
        offset, increment = find_values(offset, increment, ids, pos, i)

    return offset

result = solve()
print(f"Solution: {result}")