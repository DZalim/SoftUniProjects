price_for_strawberry = float(input())
kg_of_bananas = float(input())
kg_of_oranges = float(input())
kg_of_raspberry = float(input())
kg_of_strawberry = float(input())

price_for_raspberry = price_for_strawberry / 2
price_for_oranges = price_for_raspberry * 0.60
price_for_bananas = price_for_raspberry * 0.2

total_price = price_for_strawberry * kg_of_strawberry \
              + price_for_bananas * kg_of_bananas \
              + price_for_oranges * kg_of_oranges \
              + price_for_raspberry * kg_of_raspberry
print(f"{total_price:.2f}")
