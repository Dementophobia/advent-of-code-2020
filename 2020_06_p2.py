from aoc import read_file, timer
from functools import reduce

@timer
def solve():
    input = read_file("06") + [""]
    
    questions = []
    result = 0
    
    for line in input:
        if len(line):
            questions.append(set(line))
        else:
            result += len(reduce(lambda q1,q2: q1&q2, questions))
            questions.clear()

    return result

result = solve()
print(f"Solution: {result}")