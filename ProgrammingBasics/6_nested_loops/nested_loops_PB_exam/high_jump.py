bar_height = int(input())

current_height = bar_height - 30
number_of_total_jumps = 0
successful_jump = True

while current_height <= bar_height:
    current_jump_height = int(input())
    number_of_jumps_per_height = 0
    while current_jump_height <= current_height:
        number_of_jumps_per_height += 1
        if number_of_jumps_per_height == 3:
            successful_jump = False
            break
        current_jump_height = int(input())
    number_of_total_jumps += 1 + number_of_jumps_per_height
    if not successful_jump:
        break
    current_height += 5

if successful_jump:
    print(f"Tihomir succeeded, he jumped over {current_height - 5}cm after {number_of_total_jumps} jumps.")
else:
    print(f"Tihomir failed at {current_height}cm after {number_of_total_jumps - 1} jumps.")