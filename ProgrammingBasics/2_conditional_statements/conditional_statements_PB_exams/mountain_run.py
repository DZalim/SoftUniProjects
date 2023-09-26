import math

record_in_sec = float(input())
distance_in_metres = float(input())
time_in_sec_for_one_metre = float(input())

delay = math.floor(distance_in_metres / 50) * 30
time = distance_in_metres * time_in_sec_for_one_metre + delay
diff = abs(record_in_sec - time)

if time < record_in_sec:
    print(f"Yes! The new record is {time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")