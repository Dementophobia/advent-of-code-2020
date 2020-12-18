from aoc import read_file, timer
from re import findall

def solve_equation(equation):
    while "(" in equation:
        index = 0
        while equation[index] != ")":
            if equation[index] == "(":
                opening = index
            index += 1
        
        equation = equation[:opening] + solve_equation(equation[opening + 1:index]) + equation[index + 1:]
    
    values = [int(value) for value in findall(r"\d+", equation)]
    operators = findall(r"[\+\*]", equation)
    
    for index in range(len(operators)):
        if operators[index] == "+":  
            values[0] += values[index + 1]
        else:
            values[0] *= values[index + 1]
        
    return str(values[0])

@timer
def solve():
    raw_input = read_file("18")
    return sum((int(solve_equation(equation)) for equation in raw_input))

result = solve()
print(f"Solution: {result}")