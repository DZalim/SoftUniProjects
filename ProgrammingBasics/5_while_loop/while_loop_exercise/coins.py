money = float(input())

money = int(money * 100)

coins_counter = 0

while money != 0:
    if money >= 200:
        coins_counter += 1
        money -= 200
    elif money >= 100:
        coins_counter += 1
        money -= 100
    elif money >= 50:
        coins_counter += 1
        money -= 50
    elif money >= 20:
        coins_counter += 1
        money -= 20
    elif money >= 10:
        coins_counter += 1
        money -= 10
    elif money >= 5:
        coins_counter += 1
        money -= 5
    elif money >= 2:
        coins_counter += 1
        money -= 2
    elif money >= 1:
        coins_counter += 1
        money -= 1

print(coins_counter)
