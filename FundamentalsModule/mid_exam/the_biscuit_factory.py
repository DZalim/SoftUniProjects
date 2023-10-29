from math import floor

number_of_biscuits_per_day_per_worker = int(input())
count_of_workers_my_factory = int(input())
number_of_biscuits_for_thirty_days_competing_factory = int(input())

biscuits_for_thirty_days = 0

for day in range(1, 31):
    biscuits_per_day = number_of_biscuits_per_day_per_worker * count_of_workers_my_factory
    if day % 3 == 0:
        biscuits_per_day *= 0.75
    biscuits_for_thirty_days += floor(biscuits_per_day)

print(f"You have produced {biscuits_for_thirty_days} biscuits for the past month.")
difference = (abs(biscuits_for_thirty_days - number_of_biscuits_for_thirty_days_competing_factory) / number_of_biscuits_for_thirty_days_competing_factory) * 100
if biscuits_for_thirty_days > number_of_biscuits_for_thirty_days_competing_factory:
    print(f"You produce {difference:.2f} percent more biscuits.")
else:
    print(f"You produce {difference:.2f} percent less biscuits.")
