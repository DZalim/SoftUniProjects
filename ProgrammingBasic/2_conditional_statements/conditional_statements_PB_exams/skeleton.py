minutes_control = int(input())
seconds_control = int(input())
chute_length_in_m = float (input())
seconds_for_100_m = int(input())

control_in_seconds = minutes_control * 60 + seconds_control
delay = (chute_length_in_m / 120) * 2.5
time = (chute_length_in_m * seconds_for_100_m) / 100 - delay
diff = abs(time - control_in_seconds)

if time <= control_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
