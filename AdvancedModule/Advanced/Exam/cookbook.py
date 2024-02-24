def cookbook(*args):

    dict_of_recipes = {}

    for recipe in args:
        name_of_recipe = recipe[0]
        cuisine = recipe[1]
        list_of_ingredients = recipe[2]

        if cuisine not in dict_of_recipes.keys():
            dict_of_recipes[cuisine] = {}
        dict_of_recipes[cuisine][name_of_recipe] = list_of_ingredients

    sorted_dict = sorted(dict_of_recipes.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ''

    for cuisine, recipes in sorted_dict:
        result += f'{cuisine} cuisine contains {len(recipes)} recipes:\n'
        for recipe_name, recipe_ingredients in sorted(recipes.items()):
            result += f"  * {recipe_name} -> Ingredients: {', '.join(recipe_ingredients)}\n"

    return result


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
