import os

command_info = input()
while command_info != 'End':
    command,  *info = command_info.split('-')
    file_name = info[0]
    file_path = os.path.join('resources', file_name)

    if command == 'Create':
        with open(file_path, 'w'): pass

    elif command == 'Add':
        content = info[1]
        with open(file_path, 'a') as file:
            file.write(f'{content}\n')

    elif command == "Replace":
        old_string = info[1]
        new_string = info[2]

        try:
            with open(file_path, 'r+') as file:
                text = file.read()
                text = text.replace(old_string, new_string)

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")
    elif command == 'Delete':
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")

    command_info = input()
