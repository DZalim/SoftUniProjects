number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
holiday = input()

price_per_chrysanthemums = 0
price_per_rose = 0
price_per_tulip = 0
bouquet = 2


if season == "Spring" or season == "Summer":
    price_per_chrysanthemums = 2
    price_per_rose = 4.10
    price_per_tulip = 2.50
elif season == "Autumn" or season == "Winter":
    price_per_chrysanthemums = 3.75
    price_per_rose = 4.50
    price_per_tulip = 4.15

if holiday == "Y":
    price_per_chrysanthemums *= 1.15
    price_per_rose *= 1.15
    price_per_tulip *= 1.15

price_flowers = number_of_chrysanthemums * price_per_chrysanthemums \
                + number_of_roses * price_per_rose + number_of_tulips * price_per_tulip

if number_of_tulips > 7 and season == "Spring":
    price_flowers *= 0.95
if number_of_roses >= 10 and season == "Winter":
    price_flowers *= 0.90
if number_of_tulips + number_of_roses + number_of_chrysanthemums > 20:
    price_flowers *= 0.80

price_per_bouquet =  price_flowers + bouquet

print(f"{price_per_bouquet:.2f}")