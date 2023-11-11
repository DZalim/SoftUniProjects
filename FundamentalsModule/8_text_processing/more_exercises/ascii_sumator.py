first_character = input()
last_character = input()
string = input()

total_sum = 0

for character in string:
    if ord(first_character) < ord(character) < ord(last_character):
        total_sum += ord(character)

print(total_sum)
