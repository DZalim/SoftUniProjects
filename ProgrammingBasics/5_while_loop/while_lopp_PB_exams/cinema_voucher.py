sum_of_vaucher = int(input())

film = 0
other = 0
total_amount_sum = 0

purchase = input()
while purchase != "End":
    if len(purchase) > 8:
        price = int(ord(purchase[0]) + ord(purchase[1]))
        total_amount_sum += price
        if sum_of_vaucher >= total_amount_sum:
            film += 1
    else:
        price = int(ord(purchase[0]))
        total_amount_sum += price
        if sum_of_vaucher >= total_amount_sum:
            other += 1
    if total_amount_sum > sum_of_vaucher:
            break
    purchase = input()

print(film)
print(other)


