def shop_from_grocery_list(budget, grocery_list, *products):
    spend_money = 0
    bought_products = set()

    for product, price in products:
        if product in grocery_list and product not in bought_products:
            if price + spend_money <= budget:
                spend_money += price
                bought_products.add(product)
            else:
                break

    if len(grocery_list) == len(bought_products):
        return f"Shopping is successful. Remaining budget: {(budget - spend_money):.2f}."
    else:
        difference = set(grocery_list) - bought_products
        return f"You did not buy all the products. Missing products: {', '.join(sorted(difference))}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
