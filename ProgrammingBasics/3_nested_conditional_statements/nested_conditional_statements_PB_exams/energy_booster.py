fruit = input()
size = input()
number_of_sets = int(input())

small_set = 2
big_set = 5
price = 0

if size == "small":
    if fruit == "Watermelon":
        price = 56 * small_set
    elif fruit == "Mango":
        price = 36.66 * small_set
    elif fruit == "Pineapple":
        price = 42.10 * small_set
    elif fruit == "Raspberry":
        price = 20 * small_set
elif size == "big":
    if fruit == "Watermelon":
        price = 28.70 * big_set
    elif fruit == "Mango":
        price = 19.60 * big_set
    elif fruit == "Pineapple":
        price = 24.80 * big_set
    elif fruit == "Raspberry":
        price = 15.20 * big_set

total_price = number_of_sets * price

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} lv.")