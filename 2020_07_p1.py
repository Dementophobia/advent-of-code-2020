from aoc import read_file, timer
from collections import defaultdict
import re

def get_bag_hierachy(input):
    bag_hierachy  = defaultdict(set)
    reg_container = re.compile('^([a-z]+ [a-z]+)')
    reg_contains  = re.compile('\d+ ([a-z]+ [a-z]+)')
    
    for line in input:
        container = reg_container.findall(line)
        for bag in reg_contains.findall(line):
            bag_hierachy[bag].update(container)

    return bag_hierachy

def can_be_in_bag(bag, bag_hierachy):
    bags = set(bag_hierachy[bag])
    
    for container_bag in bag_hierachy[bag]:
        bags.update(can_be_in_bag(container_bag, bag_hierachy))

    return bags

@timer
def solve():
    input = read_file("07")
    return len(can_be_in_bag("shiny gold", get_bag_hierachy(input)))

result = solve()
print(f"Solution: {result}")