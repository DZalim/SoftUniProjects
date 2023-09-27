word = input()

current_list = []

for letter in range(len(word)):
    if word[letter].isupper():
        current_list.append(letter)

print(current_list)