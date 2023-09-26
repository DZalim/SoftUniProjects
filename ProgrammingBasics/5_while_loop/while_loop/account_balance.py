total_money = 0

while True:
    balance = input()
    if balance == "NoMoreMoney":
        break
    else:
        balance = float(balance)
        if balance < 0:
            print("Invalid operation!")
            break

        else:
            total_money += balance
            print(f"Increase: {balance:.2f}")

print(f"Total: {total_money:.2f}")