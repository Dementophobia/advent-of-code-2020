from aoc import read_file, timer
from re import findall

@timer
def solve():
    raw_input = read_file("13")
    start = int(raw_input[0])
    ids   = [int(id) for id in findall(r'\d+', raw_input[1])]
    
    wait_time = 0
    
    while 0 not in (diff := [(start + wait_time) % id for id in ids]):
        wait_time += 1
           
    return wait_time * ids[diff.index(0)]

result = solve()
print(f"Solution: {result}")