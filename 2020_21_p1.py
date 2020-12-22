from aoc import read_file, timer
from re import match, sub
from collections import defaultdict

def analyse_input(raw_input):
    allergens_dict  = defaultdict(list)
    all_ingredients = []
    
    for line in raw_input:
        ingredients, allergens = [words.split() for words in match(r"((?:(?:\w+) )+)\(contains ((?:(?:\w+) *)+)\)", sub(",", "", line)).group(1, 2)]

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
    identified_ingredients = set()
    
    while len(allergens_in_food):
        allergen, ingredient = identify_allergen(allergens_in_food)
        eliminate_combo(allergens_in_food, allergen, ingredient)
        identified_ingredients.add(ingredient)

    return sum([ingredient not in identified_ingredients for ingredient in all_ingredients])

result = solve()
print(f"Solution: {result}")