sequence_of_numbers = [int(number) for number in input().split()]
average_number = sum(sequence_of_numbers) / len(sequence_of_numbers)

numbers_greater_than_average = [number for number in sequence_of_numbers if number > average_number]
sorted_numbers = sorted(numbers_greater_than_average, reverse=True)

if len(sorted_numbers) > 4:
    numbers_for_print = [sorted_numbers[number] for number in range(5)]
    print(" ".join(str(number) for number in numbers_for_print))
elif sorted_numbers:
    print(" ".join(str(number) for number in sorted_numbers))
else:
    print("No")
