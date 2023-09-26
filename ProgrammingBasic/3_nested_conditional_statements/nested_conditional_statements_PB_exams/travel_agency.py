city = input()
packet = input()
discount = input()
days = int(input())

price_per_day = 0
DataError = False
incorrect_days = False

if city == "Bansko" or city == "Borovets":
    if packet == "withEquipment":
        price_per_day = 100
        if discount == "yes":
            price_per_day *= 0.90
    elif packet == "noEquipment":
        price_per_day = 80
        if discount == "yes":
            price_per_day *= 0.95
    else:
        DataError = True
elif city == "Varna" or city == "Burgas":
    if packet == "withBreakfast":
        price_per_day = 130
        if discount == "yes":
            price_per_day *= 0.88
    elif packet == "noBreakfast":
        price_per_day = 100
        if discount == "yes":
            price_per_day *= 0.93
    else:
        DataError = True
else:
    DataError = True

total_price = price_per_day * days

if days > 7:
    total_price = price_per_day * (days - 1)

if days < 1:
    incorrect_days = True

if not incorrect_days == False:
    print("Days must be positive number!")
elif not DataError == False:
    print("Invalid input!")
elif not DataError == True:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")


