from aoc import read_file, timer

@timer
def solve():
    raw_input = read_file("12")
    x, y, dir = 0, 0, 1
    
    for instruction in raw_input:
        op, value = instruction[0], int("".join(instruction[1:]))
        
        if   op == "N" or (op == "F" and dir == 0):
            y -= value
            
        elif op == "E" or (op == "F" and dir == 1):
            x += value
            
        elif op == "S" or (op == "F" and dir == 2):
            y += value
            
        elif op == "W" or (op == "F" and dir == 3):
            x -= value
            
        elif op == "R":
            dir = (dir + value // 90) % 4
            
        elif op == "L":
            dir = (dir - value // 90) % 4
       
    return abs(x) + abs(y)

result = solve()
print(f"Solution: {result}")