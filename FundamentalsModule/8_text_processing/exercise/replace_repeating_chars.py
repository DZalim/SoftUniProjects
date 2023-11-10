sequence_of_the_same_letters = input()

last_char = ""
final_string = ""

for char in sequence_of_the_same_letters:
    if char != last_char:
        final_string += char
        last_char = char

print(final_string)
