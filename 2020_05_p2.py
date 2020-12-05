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
    seats = sorted(read_file("05"), key = lambda s: s[7:])
    seats = sorted(seats, key = lambda s: s[:7], reverse = True)

    for i in range(len(seats)):
        current_id = calc_seat_id(seats[i])
        if i and prev_id + 2 == current_id:
            return prev_id + 1
        prev_id = current_id

result = solve()
print(f"Solution: {result}")