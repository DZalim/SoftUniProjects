season = input()
km_for_month = float(input())

price_per_km = 0

if km_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.90
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < km_for_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    elif season == "Winter":
        price_per_km = 1.25
elif 10000 < km_for_month <= 20000:
    price_per_km = 1.45

salary_per_month = price_per_km * km_for_month
salary_per_season = salary_per_month * 4
salary_without_tax = salary_per_season * 0.90

print(f"{salary_without_tax:.2f}")