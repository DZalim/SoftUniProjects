import math

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
price_for_gift = float(input())

price_per_magnolia = 3.25
price_per_hyacinths = 4
price_per_rose = 3.50
price_per_cacti = 8
tax = 0.05

total_sum = (number_of_magnolias * price_per_magnolia \
            + number_of_hyacinths * price_per_hyacinths \
            + number_of_roses * price_per_rose \
            + number_of_cacti * price_per_cacti) * 0.95

diff = abs(price_for_gift - total_sum)

if total_sum >= price_for_gift:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")