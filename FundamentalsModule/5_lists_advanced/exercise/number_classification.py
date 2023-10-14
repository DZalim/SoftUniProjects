def positive_numbers(list_of_numbers):
    return ", ".join([str(positive) for positive in list_of_numbers if positive >= 0])


def negative_numbers(list_of_numbers):
    return ", ".join([str(positive) for positive in list_of_numbers if positive < 0])


def even_numbers(list_of_numbers):
    return ", ".join([str(positive) for positive in list_of_numbers if positive % 2 == 0])


def odd_numbers(list_of_numbers):
    return ", ".join([str(positive) for positive in list_of_numbers if positive % 2 != 0])


sequence_of_numbers = [int(number) for number in input().split(", ")]

print(f"Positive: {positive_numbers(sequence_of_numbers)}")
print(f"Negative: {negative_numbers(sequence_of_numbers)}")
print(f"Even: {even_numbers(sequence_of_numbers)}")
print(f"Odd: {odd_numbers(sequence_of_numbers)}")
