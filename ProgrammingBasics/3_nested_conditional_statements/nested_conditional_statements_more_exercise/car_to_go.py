budget = float(input())
season = input()

type_of_car = ""
class_of_car = ""
price = 0

if budget <= 100:
    class_of_car = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = 0.35 * budget
    elif season == "Winter":
        type_of_car = "Jeep"
        price = 0.65 * budget
elif 100 < budget <= 500:
    class_of_car = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price = 0.45 * budget
    elif season == "Winter":
        type_of_car = "Jeep"
        price = 0.80 * budget
else:
    class_of_car = "Luxury class"
    type_of_car = "Jeep"
    price = 0.90 * budget

print(f"{class_of_car}")
print(f"{type_of_car} - {price:.2f}")
