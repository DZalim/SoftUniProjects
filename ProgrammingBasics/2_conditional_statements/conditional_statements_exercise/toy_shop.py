needed_price_for_excursion = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minions_price = 8.20
trucks_price = 2

total_price = puzzle_price * number_of_puzzles \
              + doll_price * number_of_dolls \
              + bear_price * number_of_bears \
              + minions_price * number_of_minions \
              + trucks_price * number_of_trucks

total_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks

if total_toys >= 50:
    total_price *= 0.75

total_price *= 0.90

diff = abs(needed_price_for_excursion - total_price)

if needed_price_for_excursion <= total_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
