number_of_pieces = int(input())

pieces_dict_with_composer_and_key = {}

for piece in range(number_of_pieces):
    current_piece, current_composer, current_key = input().split("|")
    if current_piece not in pieces_dict_with_composer_and_key.keys():
        pieces_dict_with_composer_and_key[current_piece] = {current_composer: current_key}
    else:
        if current_composer not in pieces_dict_with_composer_and_key[current_piece].keys():
            pieces_dict_with_composer_and_key[current_piece][current_composer] = current_key

command = input()
while command != "Stop":
    split_command = command.split("|")
    action = split_command[0]
    if action == "Add":
        piece_to_add, composer_to_add, key_to_add = split_command[1], split_command[2], split_command[3]
        if piece_to_add not in pieces_dict_with_composer_and_key.keys():
            pieces_dict_with_composer_and_key[piece_to_add] = {composer_to_add: key_to_add}
            print(f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")
        else:
            print(f"{piece_to_add} is already in the collection!")
    elif action == "Remove":
        piece_to_remove = split_command[1]
        if piece_to_remove not in pieces_dict_with_composer_and_key.keys():
            print(f"Invalid operation! {piece_to_remove} does not exist in the collection.")
        else:
            del pieces_dict_with_composer_and_key[piece_to_remove]
            print(f"Successfully removed {piece_to_remove}!")
    elif action == "ChangeKey":
        piece_to_change, key_to_change = split_command[1], split_command[2]
        if piece_to_change in pieces_dict_with_composer_and_key.keys():
            for piece, piece_values in pieces_dict_with_composer_and_key.items():
                for composer, key in piece_values.items():
                    if piece_to_change == piece:
                        pieces_dict_with_composer_and_key[piece_to_change][composer] = key_to_change
            print(f"Changed the key of {piece_to_change} to {key_to_change}!")
        else:
            print(f"Invalid operation! {piece_to_change} does not exist in the collection.")
    command = input()

for piece, piece_value in pieces_dict_with_composer_and_key.items():
    for composer, key in piece_value.items():
        print(f"{piece} -> Composer: {composer}, Key: {key}")
