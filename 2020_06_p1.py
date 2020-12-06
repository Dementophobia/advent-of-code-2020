from aoc import read_file, timer

@timer
def solve():
    input = read_file("06") + [""]
    
    questions = set()
    result = 0
    
    for line in input:
        if len(line):
            questions.update(set(line))
        else:
            result += len(questions)
            questions = set()

    return result

result = solve()
print(f"Solution: {result}")