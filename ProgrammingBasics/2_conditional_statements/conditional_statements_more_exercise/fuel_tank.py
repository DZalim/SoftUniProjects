fuel = input()
litres = float(input())

if fuel == "Diesel":
    if litres < 25:
        print(f"Fill your tank with {str.lower(fuel)}!")
    else:
        print(f"You have enough {str.lower(fuel)}.")
elif fuel == "Gasoline":
    if litres < 25:
        print(f"Fill your tank with {str.lower(fuel)}!")
    else:
        print(f"You have enough {str.lower(fuel)}.")
elif fuel == "Gas":
    if litres < 25:
        print(f"Fill your tank with {str.lower(fuel)}!")
    else:
        print(f"You have enough {str.lower(fuel)}.")
else:
    print("Invalid fuel!")