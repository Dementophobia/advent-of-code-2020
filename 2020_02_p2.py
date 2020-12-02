from aoc import read_file, timer
import re

@timer
def solve():
    reg = re.compile('(\d*)-(\d*) (\w): (\w*)')
    return sum([(password[int(pos_1)-1] == char) ^ (password[int(pos_2)-1] == char) for pos_1, pos_2, char, password in reg.findall(' '.join(read_file("02")))])

result = solve()
print(f"Solution: {result}")