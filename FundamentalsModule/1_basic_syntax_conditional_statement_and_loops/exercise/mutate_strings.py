first_word = input()
last_word = input()

last_printed_word = first_word

for iteration in range (len(first_word)):
    new_word = ""
    left_side = last_word[:iteration+1]
    right_side = first_word[iteration+1:]
    new_word = left_side + right_side
    if last_printed_word == new_word:
        continue
    else:
        last_printed_word = new_word
        print(new_word)
