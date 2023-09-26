count_of_numbers = int(input())

sum_of_letters = 0

for letter in range(count_of_numbers):
    current_letter = input()
    sum_of_letters += ord(current_letter)

print(f"The sum equals: {sum_of_letters}")