number_of_clients = int(input())

total_price = 0

for client in range (number_of_clients):
    name_of_product = input()
    total_price_per_client = 0
    total_products = 0
    while name_of_product != "Finish":
        if name_of_product == "basket":
            price = 1.50
        elif name_of_product == "wreath":
            price = 3.80
        elif name_of_product == "chocolate bunny":
            price = 7
        total_products += 1
        total_price_per_client += price
        name_of_product = input()
    if total_products % 2 == 0:
        total_price_per_client *= 0.80
    print(f"You purchased {total_products} items for {total_price_per_client:.2f} leva.")
    total_price += total_price_per_client

average_price = total_price / number_of_clients
print(f"Average bill per client is: {average_price:.2f} leva.")