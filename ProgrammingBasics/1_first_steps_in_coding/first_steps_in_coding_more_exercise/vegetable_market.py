price_per_kg_veg = float(input())
price_per_kg_fruit = float (input())
kg_veg = float(input())
kg_fruit = float(input())

euro = 1.94

sum = ((price_per_kg_veg / euro) * kg_veg + (price_per_kg_fruit / euro) * kg_fruit)

print (f"{sum:.2f}")


