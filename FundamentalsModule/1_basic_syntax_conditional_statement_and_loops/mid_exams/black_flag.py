days_of_the_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days_of_the_plunder + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        total_plunder *= 0.70

percentage = total_plunder / expected_plunder * 100

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")