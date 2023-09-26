start_range = int(input())
end_range = int(input())
magic_number = int(input())

counter = 0
found_combination = False

for number_one in range(start_range, end_range + 1):
    for number_two in range(start_range, end_range + 1):
        counter += 1
        if number_one + number_two == magic_number:
            found_combination = True
            if found_combination:
                print(f"Combination N:{counter} ({number_one} + {number_two} = {magic_number})")
                break
    if found_combination:
        break

if not found_combination:
    print(f"{counter} combinations - neither equals {magic_number}")