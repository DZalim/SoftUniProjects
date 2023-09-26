start_number = int(input())
end_number = int(input())
magic_number = int(input())

is_combined = False
counter = 0

for x in range (start_number, end_number + 1):
    for y in range (start_number, end_number + 1):
        counter += 1
        if x + y == magic_number:
            print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
            is_combined = True
            break
    if is_combined:
        break

if not is_combined:
    print(f"{counter} combinations - neither equals {magic_number}")
