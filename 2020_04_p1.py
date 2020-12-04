from aoc import read_file, timer
import re

@timer
def solve():
    input = read_file("04") + [""]
    
    reg = re.compile('(\w*):')
    all_fields = set()
    result = 0
    
    for line in input:
        if len(fields_of_line := reg.findall(line)):
            all_fields.update(fields_of_line)
        else:
            all_fields.discard("cid")
            if all_fields == {'ecl', 'eyr', 'byr', 'iyr', 'hcl', 'hgt', 'pid'}:
                result += 1
            all_fields = set()

    return result

result = solve()
print(f"Solution: {result}")