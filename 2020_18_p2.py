from aoc import read_file, timer
from re import findall
from functools import reduce

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
    
    while "+" in operators:
        index = operators.index("+")
        values = values[:index] + [values[index] + values[index + 1]] + values[index + 2:]
        operators.remove("+")

    return str(reduce(lambda a, b: a * b, [int(value) for value in values]))

@timer
def solve():
    raw_input = read_file("18")
    return sum((int(solve_equation(equation)) for equation in raw_input))

result = solve()
print(f"Solution: {result}")