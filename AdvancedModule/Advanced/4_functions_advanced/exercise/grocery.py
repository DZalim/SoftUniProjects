def grocery_store(**products):
    sorted_products = sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    result = []

    for key, value in sorted_products:
        result.append(f'{key}: {value}')

    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


def grocery_store_second(**products):
    sorted_products = sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    return '\n'.join(f'{key}: {value}' for key, value in sorted_products)


print(grocery_store_second(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store_second(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
