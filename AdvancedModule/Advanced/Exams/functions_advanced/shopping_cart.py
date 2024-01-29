def shopping_cart(*products):

    limited_products = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }

    products_list = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }

    index = 0

    while products[index] != 'Stop':
        meal, product = products[index]

        if len(products_list[meal]) < limited_products[meal] and product not in products_list[meal]:
            products_list[meal].append(product)

        index += 1

    len_of_products = sum(len(value) for value in products_list.values())

    if len_of_products > 0:
        sorted_shopping_cart = sorted(products_list.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
        result = ''

        for meal, products in sorted_shopping_cart:
            result += f'{meal}:\n'
            for product in sorted(products):
                result += f' - {product}\n'
    else:
        result = f"No products in the cart!"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
