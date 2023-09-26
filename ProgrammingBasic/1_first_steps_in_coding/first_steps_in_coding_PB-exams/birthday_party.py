rent_fee_for_the_hall = float(input())

cake = 0.20 * rent_fee_for_the_hall
drinks = cake * 0.55
animator = (1/3) * rent_fee_for_the_hall

total = rent_fee_for_the_hall + cake + drinks + animator

print(total)