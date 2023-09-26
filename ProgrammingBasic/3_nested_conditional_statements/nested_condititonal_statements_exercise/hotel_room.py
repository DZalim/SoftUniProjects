month = input()
number_of_overnight_stays = int(input())

price_apartment = 0
price_studio = 0

if month == "May" or month == "October":
    price_studio = 50
    price_apartment = 65
    if number_of_overnight_stays > 14:
        price_studio *= 0.70
        price_apartment *= 0.90
    elif number_of_overnight_stays > 7:
        price_studio *= 0.95
elif month == "June" or month == "September":
    price_studio = 75.20
    price_apartment = 68.70
    if number_of_overnight_stays > 14:
        price_studio *= 0.80
        price_apartment *= 0.90
elif month == "July" or month == "August":
    price_studio = 76
    price_apartment = 77
    if number_of_overnight_stays > 14:
        price_apartment *= 0.90

total_sum_apartment = number_of_overnight_stays * price_apartment
total_sum_studio = number_of_overnight_stays * price_studio

print(f"Apartment: {total_sum_apartment:.2f} lv.")
print(f"Studio: {total_sum_studio:.2f} lv.")
