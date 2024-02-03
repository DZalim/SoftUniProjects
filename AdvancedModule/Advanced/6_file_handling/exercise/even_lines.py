import os

file_name = 'even_lines_text.txt'
file_path = os.path.join('resources', file_name)

symbols_to_replace = ("-", ",", ".", "!", "?")

with open(file_path) as file:
    lines = file.readlines()

for line_index in range(0, len(lines), 2):
    for symbol in symbols_to_replace:
        lines[line_index] = lines[line_index].replace(symbol, '@')

    split_text = lines[line_index].split()
    reverse_split_text = split_text[::-1]
    print(' '.join(word for word in reverse_split_text))
