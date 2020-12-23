from aoc import read_file, timer

def initialize():
    raw_input = [int(cup) for cup in read_file("23")[0]]
    cups = {raw_input[i]: raw_input[i + 1] for i in range(8)}
    cups[raw_input[8]] = raw_input[0]
    
    return cups, raw_input[0]

def move(cups, current_cup):
    cup = current_cup
    taken = [(cup := cups[cup]) for i in range(3)]
            
    destination = current_cup - 1
    while not destination or destination in taken:
        if not destination:
            destination = 9
        else:
            destination -= 1
    
    cups[current_cup], cups[destination], cups[taken[-1]] = cups[taken[-1]], cups[current_cup], cups[destination]
    
    return cups, cups[current_cup]
    
@timer
def solve():
    cups, current_cup = initialize()
    
    for _ in range(100):
        cups, current_cup = move(cups, current_cup)
    
    cup = 1
    return "".join([str((cup := cups[cup])) for _ in range(8)])

result = solve()
print(f"Solution: {result}")