
saved_money = 0

destination = input()
while destination != "End":
    budget = float(input())
    saved = float(input())
    while True:
        saved_money += saved
        if saved_money >= budget:
            print(f"Going to {destination}!")
            break
        saved = float(input())
    saved_money = 0
    destination = input()

