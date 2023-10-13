current_text = input()

letter_for_remove = ["a", "o", "u", "e", "i"]

print_text = (letter for letter in current_text if letter.lower() not in letter_for_remove)

print("".join(print_text))