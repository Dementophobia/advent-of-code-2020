from aoc import read_file, timer

def calc_seat_id(seat):
    row_low, row_high = 0, 127
    col_low, col_high = 0, 7
        
    for char in seat[:7]:
        if char == "B":
            row_low  += (row_high - row_low + 1) // 2
        else:
            row_high -= (row_high - row_low + 1) // 2

    for char in seat[7:]:
        if char == "R":
            col_low  += (col_high - col_low + 1) // 2
        else:
            col_high -= (col_high - col_low + 1) // 2
    
    return row_low * 8 + col_low

@timer
def solve():
    input = read_file("05")

    seats = sorted(input, key = lambda s: s[7:])
    seats = sorted(seats, key = lambda s: s[:7], reverse = True)
    
    return calc_seat_id(seat) 

result = solve()
print(f"Solution: {result}")