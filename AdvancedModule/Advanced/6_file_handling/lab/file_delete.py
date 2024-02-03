import os

file_name_to_delete = 'my_first_file_to_delete.txt'
file_path_to_delete = os.path.join('resources', file_name_to_delete)

try:
    os.remove(file_path_to_delete)
except FileNotFoundError:
    print('File already deleted!')
