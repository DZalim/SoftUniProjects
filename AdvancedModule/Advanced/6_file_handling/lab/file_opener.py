import os

file_name = 'text.txt'
file_path = os.path.join('resources', file_name)

try:
    file = open(file_path)
    print('File found')
    file.close()
except FileNotFoundError:
    print('File not found')
