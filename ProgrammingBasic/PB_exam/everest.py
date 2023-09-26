
starting_metres = 5364
end_metres = 8848
max_days = 5
climbing_days = 1
goal_reached = False
time_end = False

continue_climbing = input()
while continue_climbing != "END":
    climbed_metres = input()
    if continue_climbing == "Yes":
        climbing_days += 1
    if climbing_days > max_days:
        time_end = True
        break
    current_climbed_metres = int(climbed_metres)
    starting_metres += current_climbed_metres
    if starting_metres >= end_metres:
        goal_reached = True
        break
    continue_climbing = input()

if goal_reached:
    print(f"Goal reached for {climbing_days} days!")
else:
    print("Failed!")
    print(f"{starting_metres}")
