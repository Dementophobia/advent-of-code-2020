from aoc import read_file, timer

@timer
def solve():
    card_public, door_public = [int(key) for key in read_file("25")]
    value = 1
    loop_size = 0

    while value != card_public:
        value = (value * 7) % 20201227
        loop_size += 1
    
    value = 1
    for i in range(loop_size):
        value = (value * door_public) % 20201227
        
        
    return value

result = solve()
print(f"Solution: {result}")