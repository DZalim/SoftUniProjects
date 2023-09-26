number_of_juniors = int(input())
number_of_seniors = int(input())
track_type = input()

tax = 0
expenses = 0

if track_type == "trail":
    tax = number_of_juniors * 5.50 + number_of_seniors * 7
elif track_type == "cross-country":
    tax = number_of_juniors * 8 + number_of_seniors * 9.50
    if number_of_seniors + number_of_juniors >= 50:
        tax *= 0.75
elif track_type == "downhill":
    tax = number_of_juniors * 12.25 + number_of_seniors * 13.75
elif track_type == "road":
    tax = number_of_juniors * 20 + number_of_seniors * 21.50

expenses = tax * 0.05

sum = tax - expenses

print(f"{sum:.2f}")
