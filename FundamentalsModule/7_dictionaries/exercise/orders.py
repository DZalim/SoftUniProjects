command = input()

my_orders_dict = {}

while command != "buy":
    product, current_price, current_quantity = command.split()
    current_price = float(current_price)
    current_quantity = int(current_quantity)
    if product not in my_orders_dict.keys():
        my_orders_dict[product] = [0, 0]
    my_orders_dict[product][0] = current_price
    my_orders_dict[product][1] += current_quantity
    command = input()

for product_name, price_quantity in my_orders_dict.items():
    total_price = price_quantity[0] * price_quantity[1]
    print(f"{product_name} -> {total_price:.2f}")
