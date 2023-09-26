number_of_lines = int(input())

last_brackets = ""
opening = ""
closing = ""

for string in range (number_of_lines):
    current_string = input()
    if current_string == "(":
        if number_of_lines == 0:
           last_brackets == current_string
           opening += current_string
        elif number_of_lines > 0 and last_brackets == ")":
            opening += current_string
    elif current_string == ")" and last_brackets:
        closing += current_string

if len(opening) == len(closing):
    print("BALANCED")
else:
    print("UNBALANCED")
