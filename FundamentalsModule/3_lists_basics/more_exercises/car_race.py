sequence_of_numbers_in_str = input().split()

sequence_of_numbers_in_int = []
for number in sequence_of_numbers_in_str:
    sequence_of_numbers_in_int.append(int(number))

left_racer = []
right_racer = []

for racer in range(len(sequence_of_numbers_in_int)//2):
    left_racer_range = sequence_of_numbers_in_int[:len(sequence_of_numbers_in_int)//2:]
    right_racer_range = sequence_of_numbers_in_int[len(sequence_of_numbers_in_int):len(sequence_of_numbers_in_int)//2:-1]
    left_racer.append(left_racer_range[racer])
    right_racer.append(right_racer_range[racer])

time_for_left_racer = 0
time_for_right_racer = 0
for time in range(len(left_racer)): #len(right_racer)
    time_for_left_racer += left_racer[time]
    time_for_right_racer += right_racer[time]
    if left_racer[time] == 0:
        time_for_left_racer *= 0.8
    if right_racer[time] == 0:
        time_for_right_racer *= 0.8

if time_for_left_racer < time_for_right_racer:
    winner = "left"
    winner_time = time_for_left_racer
else:
    winner = "right"
    winner_time = time_for_right_racer

print(f"The winner is {winner} with total time: {winner_time:.1f}")
