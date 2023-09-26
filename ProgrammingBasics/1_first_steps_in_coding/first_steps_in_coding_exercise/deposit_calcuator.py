deposit = float(input())
months = int(input())
annual_interest_precent = float(input())

annual_interest = deposit * annual_interest_precent / 100
monthly_interest = annual_interest / 12
total_sum = deposit + (months * monthly_interest)

print(total_sum)
