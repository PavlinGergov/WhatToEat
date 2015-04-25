import json
from operator import itemgetter


# Suggest recipes for today
# Take in consideration the last cooked meals
# we should NOT eat the same things every day
def suggested_for_today():
    pass


# We should have an option to buy the missing product/products using a drone!!
# This should display some markets, delivery time, etc (this is about to be discussed)
def buy_product():
    pass


# We should be able to add a recipe following the original recipes format
# If we do not have all the fields filled, we should raise an error
def add_recipe():
    pass


# Use the upper function to generate the proper return
def check_fridge():
    with open("user.json", "r") as f:
        contents = f.read()
        lst = json.loads(contents)
        products = lst[0]
    return products


# We are gona search the recipe database for an exact recipe
# Show all recipes that have the searched string:
# find: eggs with ham -> Eggs with ham and cheese, Eggs with smoked ham
def find_recipe(name):
    with open("recipes.json", "r") as f:
        result = []
        contents = f.read()
        recipes = json.loads(contents)
        for recipe in recipes:
            if name in recipe["name"]:
                result.append(recipe)
        return result


# returning a list of all recipes for wich we have sufficient products
def make_list_of_possible_recipes():
    possible_recipes = []

    with open("user.json", "r") as f:
        contents = f.read()
        lst = json.loads(contents)
        products = lst[0]

    with open("recipes.json", "r") as p:
        contents = p.read()
        recipes = json.loads(contents)

    for rec in recipes:
        is_possible = True
        for needed_product in rec["products"].keys():
            if needed_product not in products.keys():
                is_possible = False
                break
            elif rec["products"][needed_product] > products[needed_product]:
                is_possible = False
                break

        if is_possible:
            possible_recipes.append(rec)

    return possible_recipes


# sorting the possible recipes by time
def sort_by_time():
    possible_recipes = make_list_of_possible_recipes()
    return sorted(possible_recipes, key=itemgetter('time'))


# sorting the possible recipes by difficulty
def sort_by_difficulty():
    possible_recipes = make_list_of_possible_recipes()
    return sorted(possible_recipes, key=itemgetter('difficulty'))


# sorting the possible recipes by calories
def sort_by_calories():
    possible_recipes = make_list_of_possible_recipes()
    return sorted(possible_recipes, key=itemgetter('calories_for_portion'))


def sort_by_healthy():
    possible_recipes = make_list_of_possible_recipes()
    return sorted(possible_recipes, key=itemgetter('healthy'))


# @param recipe must be a valid recipe dictionary
# Cook means that we've cooked the chosen recipe
# Increase the times_cooked tag with 1
# Add date and time to the log(the log contains the recipes we've coked so far)
# Изваждаме продуктите от базата с продукти на хладилника
def cook(recipe_to_cook):

    with open("user.json", "r") as f:
        contents = f.read()
        lst = json.loads(contents)

    with open("recipes.json", "r") as p:
        contents = p.read()
        recipes = json.loads(contents)

    for product in recipe_to_cook["products"].keys():
        if product in lst[0].keys():
            lst[0][product] -= recipe_to_cook["products"][product]

    lst[1].insert(0, recipe_to_cook)
    if len(lst[1]) > 5:
        lst[1].pop()

    for recipe in recipes:
        if recipe_to_cook["id"] == recipe["id"]:
            recipe["times cooked"] += 1

    with open("user.json", "w") as f:
        json.dump(lst, f, indent=True, ensure_ascii=False)

    with open("recipes.json", "w") as p:
        json.dump(recipes, p, indent=True, ensure_ascii=False)


# We are gona return 5 recipes that were most recently cooked
def get_recent_recipes():
    with open("user.json", "r") as f:
        contents = f.read()
        lst = json.loads(contents)

    return lst[1]


# We are gona return the favourite (most cooked) recipes
def get_favourite_recipes():
    with open("recipes.json", "r") as p:
        contents = p.read()
        recipes = json.loads(contents)

    most_cooked_recipe = {"times cooked": -1}

    for recipe in recipes:
        if most_cooked_recipe["times cooked"] <= recipe["times cooked"]:
            most_cooked_recipe = recipe

    return most_cooked_recipe


# Show the ingredients(products) of the recipe
# after each product we should have: available tag -> True/False
# if we need 5 eggs and we have 4 -> avaiable(eggs) -> False
def is_available(product, quantity):
    with open("user.json", "r") as f:
        contents = f.read()
        lst = json.loads(contents)

    if product not in lst[0].keys():
        return False
    if quantity > lst[0][product]:
        return False

    return True
