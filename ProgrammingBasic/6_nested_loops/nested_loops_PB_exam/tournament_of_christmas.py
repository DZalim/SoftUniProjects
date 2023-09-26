number_of_days = int(input())

total_price = 0
win_days = 0
lost_days = 0

for day in range(1, number_of_days + 1):
    name_of_game = input()
    price_per_day = 0
    win_games = 0
    lost_games = 0
    while name_of_game != "Finish":
        result = input()
        if result == "win":
            win_games += 1
            price_per_day += 20
        elif result == "lose":
            lost_games += 1
        name_of_game = input()
    if win_games > lost_games:
        win_days += 1
        price_per_day *= 1.1
    else:
        lost_days += 1
    total_price += price_per_day

if win_days > lost_days:
    total_price *= 1.2
    print(f"You won the tournament! Total raised money: {total_price:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_price:.2f}")
