sequence_of_number_between_two_letters = input().split()

total_sum = 0

for number_between_two_letters in sequence_of_number_between_two_letters:
    first_letter = number_between_two_letters[0]
    last_letter = number_between_two_letters[-1]
    number = int(number_between_two_letters[1:len(number_between_two_letters) - 1])
    if first_letter.isupper():
        total_sum += number / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        total_sum -= ord(last_letter) - 64
    elif last_letter.islower():
        total_sum += ord(last_letter) - 96

print(f"{total_sum:.2f}")
