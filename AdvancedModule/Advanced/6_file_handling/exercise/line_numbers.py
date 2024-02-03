import os
from string import punctuation


file_name = 'line_numbers_text.txt'
file_path = os.path.join('resources', file_name)

with open(file_path) as file:
    lines = file.readlines()

output_file_name = 'line_numbers_output.txt'
output_file_path = os.path.join('resources', output_file_name)

with open(output_file_path, 'a') as output_file:
    for line_index in range(len(lines)):
        letters, marks = 0, 0

        for symbol in lines[line_index]:
            if symbol.isalpha():
                letters += 1
            elif symbol in punctuation:
                marks += 1

        output_file.write(f'Line {line_index + 1}: {lines[line_index][:-1]} ({letters})({marks})\n')
