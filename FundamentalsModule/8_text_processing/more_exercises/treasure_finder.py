sequence_of_keys = input().split()

command = input()
while command != "find":
    decrypted_message = ""
    multiply_key = len(command) // len(sequence_of_keys)
    for char, key in zip(command, sequence_of_keys * multiply_key + sequence_of_keys):
        decrypted_message += chr(ord(char) - int(key))
    type_of_treasure = ""
    coordinates = ""
    find_treasure = False
    find_coordinates = False
    for index in range(len(decrypted_message)):
        if decrypted_message[index] == "&" and not find_treasure:
            for treasure in range(index+1, len(decrypted_message)):
                if decrypted_message[treasure] != "&":
                    type_of_treasure += decrypted_message[treasure]
                else:
                    find_treasure = True
                    break
        elif decrypted_message[index] == "<" and not find_coordinates:
            for coordinate in range(index + 1, len(decrypted_message)):
                if decrypted_message[coordinate] != ">":
                    coordinates += decrypted_message[coordinate]
                else:
                    find_coordinates = True
                    break
    print(f"Found {type_of_treasure} at {coordinates}")
    command = input()
