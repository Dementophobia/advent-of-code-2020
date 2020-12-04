from aoc import read_file, timer
import re

def check_byr(passport):
    value = int([fields[1] for fields in passport if fields[0] == "byr"][0])
    return value >= 1920 and value <= 2002

def check_iyr(passport):
    value = int([fields[1] for fields in passport if fields[0] == "iyr"][0])
    return value >= 2010 and value <= 2020

def check_eyr(passport):
    value = int([fields[1] for fields in passport if fields[0] == "eyr"][0])
    return value >= 2020 and value <= 2030

def check_hgt(passport):
    value = [fields[1] for fields in passport if fields[0] == "hgt"][0]
    return (value[-2:] == "cm" and int(value[:-2]) >= 150 and int(value[:-2]) <= 193) or \
           (value[-2:] == "in" and int(value[:-2]) >=  59 and int(value[:-2]) <=  76)

def check_hcl(passport):
    value = [fields[1] for fields in passport if fields[0] == "hcl"][0]
    return len(value) == 7 and value[0] == "#" and sum([char in "0123456789abcdef" for char in value[1:]]) == 6

def check_ecl(passport):
    value = [fields[1] for fields in passport if fields[0] == "ecl"][0]
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_pid(passport):
    value = [fields[1] for fields in passport if fields[0] == "pid"][0]
    return sum([char in "0123456789" for char in value]) == 9

def check_passport(passport):
    for check in [check_byr, check_iyr, check_eyr, check_hgt, check_hcl, check_ecl, check_pid]:
        if not check(passport):
            return 0
    return 1

@timer
def solve():
    input = read_file("04") + [""]
    
    reg = re.compile('(\w*):([\w#]*)')
    all_fields = set()
    result = 0
    
    for line in input:
        if len(fields_of_line := reg.findall(line)):
            all_fields.update(fields_of_line)
        else:
            entries = set(fields[0] for fields in all_fields)
            entries.discard("cid")
            if entries == {'ecl', 'eyr', 'byr', 'iyr', 'hcl', 'hgt', 'pid'} and check_passport(all_fields):
                result += 1
            all_fields = set()

    return result

result = solve()
print(f"Solution: {result}")