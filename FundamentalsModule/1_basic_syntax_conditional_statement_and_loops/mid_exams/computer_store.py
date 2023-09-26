command = input()

total_price = 0

while True:
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    total_price += price
    command = input()

taxes = total_price * 0.2
total_price_with_taxes = total_price + taxes
if command == "special":
    total_price_with_taxes *= 0.9
if total_price_with_taxes == 0:
    print("Invalid order!" )
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price_with_taxes:.2f}$")
