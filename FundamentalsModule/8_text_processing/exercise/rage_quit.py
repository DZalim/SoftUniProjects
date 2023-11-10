string_number_pairs = input().upper()

repeat_count = ""
string_to_repeat = ""
new_string = ""

for index in range(len(string_number_pairs)):
    if string_number_pairs[index].isdigit():
        repeat_count += string_number_pairs[index]
        if index + 1 < len(string_number_pairs):
            if not string_number_pairs[index + 1].isdigit():
                new_string += string_to_repeat * int(repeat_count)
                string_to_repeat = ""
        else:
            new_string += string_to_repeat * int(repeat_count)
    elif not string_number_pairs[index].isdigit():
        string_to_repeat += string_number_pairs[index]
        if string_number_pairs[index + 1].isdigit():
            repeat_count = ""

print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)
