def calculate_total_price(product, quantity):
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2
    result = price * quantity
    return result


type_of_products = input()
quantity_of_product = int(input())

result_for_print = calculate_total_price(type_of_products, quantity_of_product)
print(f"{result_for_print:.2f}")