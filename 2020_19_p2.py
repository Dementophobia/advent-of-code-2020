from aoc import read_file, timer
from re import findall
from inspect import stack

def substitute_rule(id, rules, known):
    if id in known:
        return known[id]

    if len(stack(0)) > 13:
        return ""
    
    sequence = "("
   
    for next_id in rules[id]:
        if next_id == "|":
            sequence += "|"
            continue
        next_sequence = substitute_rule(next_id, rules, known)
        known[next_id] = next_sequence
        sequence += next_sequence
    
    return sequence + ")"

@timer
def solve():
    raw_input   = read_file("19")
    raw_rules   = raw_input[:(index := raw_input.index(''))]
    messages    = raw_input[index + 1:]
    rules       = {(r := findall(r"(\d+): (.*)", rule)[0])[0]: r[1].split(" ") for rule in raw_rules}
    known       = {}
    rules["8"]  = ["42", "|", "42", "8"]
    rules["11"] = ["42", "31", "|", "42", "11", "31"]
    
    for id, rule in rules.items():
        if rule[0][0] == '"':
            known[id] = rule[0][1]
            
    rule_zero = substitute_rule("0", rules, known)
    
    return sum((len((best_match := findall(rule_zero, message))) and message == best_match[0][0] for message in messages))

result = solve()
print(f"Solution: {result}")