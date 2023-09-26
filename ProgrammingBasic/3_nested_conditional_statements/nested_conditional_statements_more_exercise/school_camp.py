season = input()
type_of_group = input()
number_of_students = int(input())
number_of_overnight_stays = int(input())

price_per_night = 0
sport = ""

if type_of_group == "girls" or type_of_group == "boys":
    if season == "Winter":
        price_per_night = 9.60
        if type_of_group == "girls":
            sport = "Gymnastics"
        elif type_of_group == "boys":
            sport = "Judo"
    elif season == "Spring":
        price_per_night = 7.20
        if type_of_group == "girls":
            sport = "Athletics"
        elif type_of_group == "boys":
            sport = "Tennis"
    elif season == "Summer":
        price_per_night = 15
        if type_of_group == "girls":
            sport = "Volleyball"
        elif type_of_group == "boys":
            sport = "Football"
elif type_of_group == "mixed":
    if season == "Winter":
        price_per_night = 10
        sport = "Ski"
    elif season == "Spring":
        price_per_night = 9.50
        sport = "Cycling"
    elif season == "Summer":
        price_per_night = 20
        sport = "Swimming"

total_price = number_of_overnight_stays * price_per_night * number_of_students

if number_of_students >= 50:
    total_price *= 0.50
elif 20 <= number_of_students < 50:
    total_price *= 0.85
elif 10 <= number_of_students < 20:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")

