n_km = int(input())
day_or_night = input()

initiation_fee_taxi = 0.70
day_for_km_taxi = 0.79
night_for_km_taxi = 0.90
day_and_night_for_km_bus = 0.09 # up to 20 km
day_and_night_for_km_train = 0.06 # up to 100 km

night_price_taxi = n_km * night_for_km_taxi + initiation_fee_taxi
day_price_taxi = n_km * day_for_km_taxi + initiation_fee_taxi
price_bus = n_km * day_and_night_for_km_bus
price_train = n_km * day_and_night_for_km_train

if n_km < 20:
    if day_or_night == "day":
        print(f"{day_price_taxi:.2f}")
    else:
        print(f"{night_price_taxi:.2f}")
elif n_km >= 100:
    if day_or_night == "day":
        lowest_price = min(price_train, price_bus, day_price_taxi)
        print(f"{lowest_price:.2f}")
    else:
        lowest_price = min(price_train, price_bus, night_price_taxi)
        print(f"{lowest_price:.2f}")
else:
    if day_or_night == "day":
        lowest_price = min(price_bus, day_price_taxi)
        print(f"{lowest_price:.2f}")
    else:
        lowest_price = min(price_bus, night_price_taxi)
        print(f"{lowest_price:.2f}")


