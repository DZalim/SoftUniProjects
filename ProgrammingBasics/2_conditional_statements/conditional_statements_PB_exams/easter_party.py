number_of_guests = int(input())
envelope_per_person = float(input())
budget = float(input())

cake = 0.10 * budget

if number_of_guests >= 10 and number_of_guests <= 15:
    envelope_per_person *= 0.85
elif number_of_guests > 15 and number_of_guests <= 20:
    envelope_per_person *= 0.8
elif number_of_guests > 20:
    envelope_per_person *= 0.75

needed_money = number_of_guests * envelope_per_person + cake
diff = abs(needed_money - budget)

if budget >= needed_money:
    print(f"It is party time! {diff:.2f} leva left.")
else:
    print(f"No party! {diff:.2f} leva needed.")