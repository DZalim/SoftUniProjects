key_number = int(input())
number_of_lines = int(input())

message = ""

for letter in range(number_of_lines):
    current_letter = input()
    current_letter_in_ord = ord(current_letter) + key_number
    message += chr(current_letter_in_ord)

print(message)
