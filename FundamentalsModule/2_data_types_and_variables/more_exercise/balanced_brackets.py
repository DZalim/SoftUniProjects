number_of_lines = int(input())

opening = ""
closing = ""
all_closing = ""
last_brackets = ""

for string in range (number_of_lines):
    current_string = input()
    if current_string == "(":
        opening += current_string
        last_brackets = "("
    elif current_string == ")":
        if last_brackets == "(":
            closing += current_string
            last_brackets = ")"
        all_closing += ")"


if len(opening) == len(closing) and len(closing) == len(all_closing):
    print("BALANCED")
else:
    print("UNBALANCED")
