from aoc import read_file, timer
from collections import defaultdict
import re

def get_bag_hierachy(input):
    bag_hierachy  = defaultdict(set)
    reg_container = re.compile('^([a-z]+ [a-z]+)')
    reg_contains  = re.compile('(\d+) ([a-z]+ [a-z]+)')
    
    for line in input:
        container = reg_container.findall(line)[0]
        for bag in reg_contains.findall(line):
            bag_hierachy[container].add(bag)

    return bag_hierachy

def contains_num_of_bags(bag, bag_hierachy):
    return sum([int(contained_bag[0]) * contains_num_of_bags(contained_bag[1], bag_hierachy) for contained_bag in bag_hierachy[bag]]) + 1

@timer
def solve():
    input = read_file("07")
    return contains_num_of_bags("shiny gold", get_bag_hierachy(input)) - 1

result = solve()
print(f"Solution: {result}")