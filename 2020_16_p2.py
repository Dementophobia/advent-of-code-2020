from aoc import read_file, timer
from re import findall
from functools import reduce

def get_fields_and_tickets():
    mode, fields, field_structure, your_ticket, nearby_tickets = 0, set(), {}, [], []
    
    for line in read_file("16"):
        if not len(line) or "ticket" in line:
            mode += 1
            continue
            
        if mode == 0:
            field = findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)[0]
            field_structure[field[0]] = [int(num) for num in field[1:]]
            fields = fields | \
                     set(value for value in range(field_structure[field[0]][0], field_structure[field[0]][1] + 1)) | \
                     set(value for value in range(field_structure[field[0]][2], field_structure[field[0]][3] + 1))

        if mode == 2:
            your_ticket = [int(value) for value in line.split(",")]

        if mode == 4:
            values = [int(num) for num in line.split(",")]
            if not sum(value not in fields for value in values):
                nearby_tickets.append(values)

    return field_structure, nearby_tickets, your_ticket

@timer
def solve():
    field_structure, nearby_tickets, your_ticket = get_fields_and_tickets()
    possible_positions = {field_name: set(range(len(field_structure))) for field_name in field_structure.keys()}
    values_in_position = [[value[i] for value in nearby_tickets] for i in range(len(nearby_tickets[0]))]
    
    for field in possible_positions.keys():
        for position in range(len(field_structure)):
            for value in values_in_position[position]:
                if not ((field_structure[field][0] <= value and field_structure[field][1] >= value) or \
                        (field_structure[field][2] <= value and field_structure[field][3] >= value)):
                    possible_positions[field].discard(position)
    
    possible_positions = {key: value for key, value in sorted(possible_positions.items(), key=lambda item: item[1])}
    
    found = set()
    
    for field, positions in possible_positions.items():
        value = positions.symmetric_difference(found)
        found.update(value)
        possible_positions[field] = int(list(value)[0])

    possible_positions = {key: value for key, value in sorted(possible_positions.items(), key=lambda item: item[1])}

    return reduce(lambda x, y: x*y, [your_ticket[possible_positions[field]] for field, position in possible_positions.items() if "departure" in field])


result = solve()
print(f"Solution: {result}")