type_of_cinema = input()
rows = int(input())
columns = int(input())

price = 0
total_places = rows * columns

if type_of_cinema == "Premiere":
    price = 12
elif type_of_cinema == "Normal":
    price = 7.5
elif type_of_cinema == "Discount":
    price = 5

total_income = price * total_places

print(f"{total_income:.2f} leva")
