from collections import deque

amount_of_money = [int(el) for el in input().split()] #stack
prices_of_foods = deque([int(el) for el in input().split()]) #queue

food_eaten = 0

while amount_of_money and prices_of_foods:
    last_amount = amount_of_money.pop()
    first_food = prices_of_foods.popleft()

    if last_amount < first_food:
        continue

    food_eaten += 1

    if last_amount > first_food:
        difference = last_amount - first_food
        if amount_of_money:
            amount_of_money[-1] += difference

if food_eaten:
    if food_eaten >= 4:
        print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
    elif food_eaten == 1:
        print(f"Henry ate: {food_eaten} food.")
    else:
        print(f"Henry ate: {food_eaten} foods.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")
