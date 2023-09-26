budget = float(input())

name_of_actor = input()
while name_of_actor != "ACTION":
    if len(name_of_actor) <= 15:
        salary = float(input())
    else:
        salary = budget * 0.20
    budget -= salary
    if budget < 0:
        break
    name_of_actor = input()

if budget >= 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {abs(budget):.2f} leva for our actors.")