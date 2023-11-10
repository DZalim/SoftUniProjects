lines_of_strings = int(input())

for string in range(lines_of_strings):
    current_string = input().split()
    name = ""
    age = ""
    for word in current_string:
        if "@" in word and "|" in word:
            first_index = 0
            last_index = 0
            for index in range(len(word)):
                if word[index] == "|":
                    last_index = index
                elif word[index] == "@":
                    first_index = index+1
            name = word[first_index:last_index]
        elif "#" in word and "*" in word:
            first_index = 0
            last_index = 0
            for index in range(len(word)):
                if word[index] == "*":
                    last_index = index
                elif word[index] == "#":
                    first_index = index+1
            age = word[first_index:last_index]
    if name.isalpha() and age.isdigit():
        print(f"{name} is {int(age)} years old.")
