def find_characters(first, second):
    all_characters = []
    for character in range(ord(first) + 1, ord(second)):
        all_characters.append(chr(character))
    return all_characters


first_character = input()
second_character = input()

returned_characters = find_characters(first_character, second_character)
print(" ".join(returned_characters))