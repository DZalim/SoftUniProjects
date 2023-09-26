quantity_of_eggs = int(input())

sold_eggs = 0

command = input()
while command != "Close":
    number_of_eggs = int(input())
    if command == "Buy":
        if quantity_of_eggs >= number_of_eggs:
            quantity_of_eggs -= number_of_eggs
            sold_eggs += number_of_eggs
        else:
            break
    elif command == "Fill":
        quantity_of_eggs += number_of_eggs
    command = input()

if command == "Close":
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {quantity_of_eggs}.")
