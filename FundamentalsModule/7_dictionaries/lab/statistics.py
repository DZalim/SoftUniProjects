data = input()

my_dict = {}

while data != "statistics":
    key, value = data.split(": ")
    value = int(value)
    if key not in my_dict:
        my_dict[key] = value
    else:
        my_dict[key] += value
    data = input()

print("Products in stock:")
for product, quantity in my_dict.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
