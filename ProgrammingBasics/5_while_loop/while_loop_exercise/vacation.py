needed_money = float(input())
available_money = float(input())

days = 0
spend_counter = 0

while available_money < needed_money:
    action = input()
    action_sum = float(input())
    days += 1
    if action == "spend":
        spend_counter += 1
        available_money -= action_sum
        if available_money < 0:
            available_money = 0
        if spend_counter == 5:
            break
    elif action == "save":
        spend_counter = 0
        available_money += action_sum

if spend_counter == 5:
    print(f"You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
