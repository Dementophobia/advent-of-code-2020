from aoc import read_file, timer

@timer
def solve():
    input = read_file("08")
    mod_pos = -1
    seen = set()

    while True:
        code = [line.split() for line in input]
        
        mod_pos += 1
        
        if code[mod_pos][0] == "jmp":
            code[mod_pos][0] = "nop"
        elif code[mod_pos][0] == "nop":
            code[mod_pos][0] = "jmp"
        else:
            continue

        accu, pos = 0, 0

        while pos not in seen:
            seen.add(pos)
            if code[pos][0] == "acc":
                accu += int(code[pos][1])
            elif code[pos][0] == "jmp":
                pos += int(code[pos][1]) - 1
            pos += 1

            if pos == len(code):
                return accu

        seen.clear()

result = solve()
print(f"Solution: {result}")