sequence_of_numbers = [int(number) for number in input().split(", ")]

current_group = 10

while sequence_of_numbers:
    print(f"Group of {current_group}'s: {[number for number in sequence_of_numbers if number <= current_group]}")
    sequence_of_numbers = [number for number in sequence_of_numbers if number > current_group]
    current_group += 10
