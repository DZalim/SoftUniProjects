start_range = input()
end_range = input()
skip_letter = input()

combinations = 0

for letter_one in range(ord(start_range), ord(end_range) + 1):
    for letter_two in range(ord(start_range), ord(end_range) + 1):
        for letter_three in range(ord(start_range), ord(end_range) + 1):
            if letter_one != ord(skip_letter) and letter_two != ord(skip_letter) and letter_three != ord(skip_letter):
                combinations += 1
                print(f"{chr(letter_one)}{chr(letter_two)}{chr(letter_three)}", end= " ")
print(combinations, end= " ")