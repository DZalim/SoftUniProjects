import math
x_area = int(input())
y_grapes_for_one_area = float(input())
z_needed_litres_vine = float(input())
number_of_workers = int(input())

area_for_vine = x_area * 0.40
grapes_for_all_area = area_for_vine * y_grapes_for_one_area
litres_vine = math.ceil(grapes_for_all_area / 2.5)

diff = abs(z_needed_litres_vine - litres_vine)
diff_floor = math.floor(diff)
diff_ceil = math.ceil(diff)
vine_for_one_worker = math.ceil(diff / number_of_workers)

if litres_vine < z_needed_litres_vine:
    print(f"It will be a tough winter! More {diff_floor} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {litres_vine} liters.")
    print(f"{diff_ceil} liters left -> {vine_for_one_worker} liters per person.")