data = input().split()

my_dict = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    my_dict[key] = value

searched_products = input().split()

for searched_product in searched_products:
    if searched_product in my_dict:
        print(f"We have {my_dict[searched_product]} of {searched_product} left")
    else:
        print(f"Sorry, we don't have {searched_product}")
