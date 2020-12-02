from aoc import read_file, timer
import re

@timer
def solve():
    reg = re.compile('(\d*)-(\d*) (\w): (\w*)')
    return sum([(occurances := password.count(char)) >= int(low) and occurances <= int(high) for low, high, char, password in reg.findall(' '.join(read_file("02")))])

result = solve()
print(f"Solution: {result}")