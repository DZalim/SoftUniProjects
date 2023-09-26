old_record = float(input())
distance_in_metres = float(input())
time_in_sec_for_metres = float(input())

delay = (distance_in_metres // 15) * 12.5

total_time = distance_in_metres * time_in_sec_for_metres + delay

diff = abs(total_time - old_record)

if total_time < old_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {diff:.2f} seconds slower.")