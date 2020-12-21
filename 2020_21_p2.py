from aoc import read_file, timer
from re import findall
from collections import defaultdict

def analyse_input(raw_input):
    allergens_dict  = defaultdict(list)
    all_ingredients = []
    
    for line in raw_input:
        words = findall(r"(\w+)", line)
        ingredients, allergens = words[:(seperator := words.index("contains"))], words[seperator + 1:]
        for allergen in allergens:
            allergens_dict[allergen].append(set(ingredients))
        all_ingredients.extend(ingredients)
    
    return allergens_dict, all_ingredients

def identify_allergen(allergens_in_food):
    for allergen, ingredients in allergens_in_food.items():
        candidates = ingredients[0].intersection(*ingredients)
        if len(candidates) == 1:
            return allergen, list(candidates)[0]

def eliminate_combo(allergens_in_food, allergen, ingredient):
    del allergens_in_food[allergen]
    for allergen in allergens_in_food.keys():
        for ingredients in allergens_in_food[allergen]:
            ingredients.discard(ingredient)          

@timer
def solve():
    allergens_in_food, all_ingredients = analyse_input(read_file("21"))
    identified_ingredients = []
    
    while len(allergens_in_food):
        allergen, ingredient = identify_allergen(allergens_in_food)
        eliminate_combo(allergens_in_food, allergen, ingredient)
        identified_ingredients.append((allergen, ingredient))

    identified_ingredients.sort(key = lambda combo: combo[0])

    return ",".join([ingredient[1] for ingredient in identified_ingredients])

result = solve()
print(f"Solution: {result}")