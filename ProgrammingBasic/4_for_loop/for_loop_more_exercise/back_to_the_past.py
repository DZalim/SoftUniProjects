inherited_money = float(input())
the_year_to_which_he_must_live = int(input())

needed_money = 0
age = 17

for year in range (1800, the_year_to_which_he_must_live + 1):
    age += 1
    if year % 2 == 0:
        needed_money += 12000
    else:
        needed_money += 12000 + 50 * age

diff = abs(needed_money - inherited_money)

if inherited_money >=needed_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")