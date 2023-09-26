term = input()
type_of_contract = input()
added_mobile_internet = input()
number_of_month_for_payment = int(input())

price_per_packet = 0
price_mobile_internet = 0

if term == "one":
    if type_of_contract == "Small":
        price_per_packet = 9.98
    elif type_of_contract == "Middle":
        price_per_packet = 18.99
    elif type_of_contract == "Large":
        price_per_packet = 25.98
    elif type_of_contract == "ExtraLarge":
        price_per_packet = 35.99
elif term == "two":
    if type_of_contract == "Small":
        price_per_packet = 8.58
    elif type_of_contract == "Middle":
        price_per_packet = 17.09
    elif type_of_contract == "Large":
        price_per_packet = 23.59
    elif type_of_contract == "ExtraLarge":
        price_per_packet = 31.79

if added_mobile_internet == "yes":
    if price_per_packet <= 10:
        price_mobile_internet = 5.50
    elif price_per_packet > 30:
        price_mobile_internet = 3.85
    else:
        price_mobile_internet = 4.35

total_payment = (price_per_packet + price_mobile_internet) * number_of_month_for_payment

if term == "two":
    total_payment *= 0.9625

print(f"{total_payment:.2f} lv.")