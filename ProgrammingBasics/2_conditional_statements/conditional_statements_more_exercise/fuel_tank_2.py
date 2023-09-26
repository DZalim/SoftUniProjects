fuel = input()
litres = float(input())
card = (input())

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

discount_gasoline = 0.18
discount_diesel = 0.12
discount_gas = 0.08

discount_between_20_and_25 = 0.08
discount_up_to_25 = 0.10

total_gasoline_price_without_discount = litres * gasoline_price
total_gasoline_price_with_discount = litres * (gasoline_price - discount_gasoline)
total_diesel_price_without_discount = litres * diesel_price
total_diesel_price_with_discount = litres * (diesel_price - discount_diesel)
total_gas_price_without_discount = litres * gas_price
total_gas_price_with_discount = litres * (gas_price - discount_gas)

if litres > 25:
    total_gasoline_price_without_discount *= 0.9
    total_gasoline_price_with_discount *= 0.9
    total_diesel_price_without_discount *= 0.9
    total_diesel_price_with_discount *= 0.9
    total_gas_price_without_discount *= 0.9
    total_gas_price_with_discount *= 0.9
elif litres >= 20 and litres <=25:
    total_gasoline_price_without_discount *= 0.92
    total_gasoline_price_with_discount *= 0.92
    total_diesel_price_without_discount *= 0.92
    total_diesel_price_with_discount *= 0.92
    total_gas_price_without_discount *= 0.92
    total_gas_price_with_discount *= 0.92

if fuel == "Gasoline":
    if card == "Yes":
        print(f"{total_gasoline_price_with_discount:.2f} lv.")
    else:
        print(f"{total_gasoline_price_without_discount:.2f} lv.")
elif fuel == "Diesel":
    if card == "Yes":
        print(f"{total_diesel_price_with_discount:.2f} lv.")
    else:
        print(f"{total_diesel_price_without_discount:.2f} lv.")
elif fuel == "Gas":
    if card == "Yes":
        print(f"{total_gas_price_with_discount:.2f} lv.")
    else:
        print(f"{total_gas_price_without_discount:.2f} lv.")



