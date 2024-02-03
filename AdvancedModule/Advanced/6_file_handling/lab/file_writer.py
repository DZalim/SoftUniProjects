import os

file_name_to_delete = 'my_first_file_to_delete.txt'
file_path_to_delete = os.path.join('resources', file_name_to_delete)

file = open(file_path_to_delete, 'a')
file.write('I just created my first file!')
file.close()


file_name = 'my_first_file.txt'
file_path = os.path.join('resources', file_name)

with open(file_path, 'a') as file:
    file.write('I just created my first file!')
