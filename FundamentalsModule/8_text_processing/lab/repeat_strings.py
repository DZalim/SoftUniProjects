sequence_of_strings = input().split()

for word in sequence_of_strings:
    current_word = word*len(word)
    print(f"{current_word}", end="")
