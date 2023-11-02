text = input()
text = text.replace(" ", "")
my_dict = {}

for letter in text:
    if letter not in my_dict:
        my_dict[letter] = 0
    my_dict[letter] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
