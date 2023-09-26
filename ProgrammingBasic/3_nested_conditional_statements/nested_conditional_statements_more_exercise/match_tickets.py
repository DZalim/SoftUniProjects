budget = float(input())
category = input()
number_of_persons = int(input())

VIP = 499.99
Normal = 249.99

transport = 0

if 1 <= number_of_persons <= 4:
    transport = 0.75 * budget
elif 5 <= number_of_persons <= 9:
    transport = 0.60 * budget
elif 10 <= number_of_persons <= 24:
    transport = 0.50 * budget
elif 25 <= number_of_persons <= 49:
    transport = 0.40 * budget
elif number_of_persons >= 50:
    transport = 0.25 * budget

left_money = budget - transport

if category == "VIP":
    needed_money_for_ticket = number_of_persons * VIP
elif category == "Normal":
    needed_money_for_ticket = number_of_persons * Normal

diff = abs(left_money - needed_money_for_ticket)

if left_money >= needed_money_for_ticket:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
