age = int(input())
laundry_price = float(input())
price_per_toy = int(input())

total_toys = 0
birthday_money = 0
total_money = 0

for birthday in range(1, age+1):
    if birthday % 2 == 0:
        birthday_money += 10
        total_money += birthday_money - 1
    else:
        total_toys +=1

saved_money = total_money + total_toys * price_per_toy
diff = abs(saved_money - laundry_price)

if saved_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
