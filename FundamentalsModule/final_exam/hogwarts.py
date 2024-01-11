spell_to_deciphered = input()

command = input()
while command != "Abracadabra":
    split_command = command.split()
    action = split_command[0]
    if action == "Abjuration":
        spell_to_deciphered = spell_to_deciphered.upper()
        print(spell_to_deciphered)
    elif action == "Necromancy":
        spell_to_deciphered = spell_to_deciphered.lower()
        print(spell_to_deciphered)
    elif action == "Illusion":
        index = int(split_command[1])
        letter = split_command[2]
        if 0 <= index < len(spell_to_deciphered):
            spell_to_deciphered = spell_to_deciphered[:index:] + letter + spell_to_deciphered[index+1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif action == "Divination":
        first_substring = split_command[1]
        second_substring = split_command[2]
        if first_substring in spell_to_deciphered:
            spell_to_deciphered = spell_to_deciphered.replace(first_substring, second_substring)
            print(spell_to_deciphered)
    elif action == "Alteration":
        substring = split_command[1]
        if substring in spell_to_deciphered:
            spell_to_deciphered = spell_to_deciphered.replace(substring, "")
            print(spell_to_deciphered)
    else:
        print("The spell did not work!")

    command = input()
