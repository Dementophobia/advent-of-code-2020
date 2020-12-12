from aoc import read_file, timer

@timer
def solve():
    raw_input = read_file("12")
    x, y, wp_x, wp_y = 0, 0, 10, -1

    directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    rot_r, rot_l = [("R", 90), ("L", 270)], [("L", 90), ("R", 270)]
    
    for instruction in raw_input:
        op, value = instruction[0], int("".join(instruction[1:]))
        
        if   op == "F":
            x, y = x + value * wp_x, y + value * wp_y
            
        elif op in ["R", "L"]:
            if value == 180:
                wp_x, wp_y = -wp_x, -wp_y
                
            elif (op, value) in rot_r:
                wp_x, wp_y = -wp_y, wp_x
            
            elif (op, value) in rot_l:
                wp_x, wp_y = wp_y, -wp_x
        
        else:
            wp_x, wp_y = wp_x + directions[op][0] * value, wp_y + directions[op][1] * value
       
    return abs(x) + abs(y)

result = solve()
print(f"Solution: {result}")