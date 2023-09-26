number_of_joinery = int(input())
type_of_joinery = input()
delivery = input()

price_per_joinery = 0
DataError = False
delivery_price = 0


if type_of_joinery == "90X130":
    price_per_joinery = 110
    if 60 > number_of_joinery > 30:
        price_per_joinery *= 0.95
    elif number_of_joinery > 60:
        price_per_joinery *= 0.92
elif type_of_joinery == "100X150":
    price_per_joinery = 140
    if 80 > number_of_joinery > 40:
        price_per_joinery *= 0.94
    elif number_of_joinery > 80:
        price_per_joinery *= 0.9
elif type_of_joinery == "130X180":
    price_per_joinery = 190
    if 50 > number_of_joinery > 20:
        price_per_joinery *= 0.93
    elif number_of_joinery > 50:
        price_per_joinery *= 0.88
elif type_of_joinery == "200X300":
    price_per_joinery = 250
    if 50 > number_of_joinery > 25:
        price_per_joinery *= 0.91
    elif number_of_joinery > 50:
        price_per_joinery *= 0.86

if delivery == "With delivery":
    delivery_price = 60

total_price = number_of_joinery * price_per_joinery + delivery_price

if number_of_joinery > 99:
    total_price *= 0.96

if number_of_joinery < 10:
    DataError = True

if not DataError == False:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
