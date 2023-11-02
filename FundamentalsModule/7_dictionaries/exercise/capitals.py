countries = input().split(", ")
capital_cities = input().split(", ")

my_dict = {country: city for country, city in zip(countries, capital_cities)}

for key, value in my_dict.items():
    print(f"{key} -> {value}")
