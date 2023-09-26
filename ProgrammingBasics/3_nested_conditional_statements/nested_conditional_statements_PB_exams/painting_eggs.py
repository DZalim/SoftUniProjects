size_of_eggs = input()
color_of_eggs = input()
number = int(input())

price = 0

if color_of_eggs == "Red":
    if size_of_eggs == "Large":
        price = 16
    elif size_of_eggs == "Medium":
        price = 13
    elif size_of_eggs == "Small":
        price = 9
elif color_of_eggs == "Green":
    if size_of_eggs == "Large":
        price = 12
    elif size_of_eggs == "Medium":
        price = 9
    elif size_of_eggs == "Small":
        price = 8
elif color_of_eggs == "Yellow":
    if size_of_eggs == "Large":
        price = 9
    elif size_of_eggs == "Medium":
        price = 7
    elif size_of_eggs == "Small":
        price = 5

total_price = price * number
revenue = total_price * 0.65

print(f"{revenue:.2f} leva.")