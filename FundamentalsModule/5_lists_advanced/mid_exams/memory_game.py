sequence_of_twin_elements = [element for element in input().split()]

moves = 1

command = input()
while command != "end":
    split_command = command.split()
    first_index = int(split_command[0])
    second_index = int(split_command[1])
    if (first_index != second_index) and\
            (0 <= first_index < len(sequence_of_twin_elements)) and\
            (0 <= second_index < len(sequence_of_twin_elements)):
        if sequence_of_twin_elements[first_index] == sequence_of_twin_elements[second_index]:
            print(f"Congrats! You have found matching elements - {sequence_of_twin_elements[first_index]}!")
            match_element = sequence_of_twin_elements[first_index]
            for remove_element in range(len(sequence_of_twin_elements) - 1, -1, -1):
                if match_element == sequence_of_twin_elements[remove_element]:
                    sequence_of_twin_elements.remove(match_element)
        else:
            print("Try again!")
    else:
        print("Invalid input! Adding additional elements to the board")
        middle_of_list = len(sequence_of_twin_elements)//2
        sequence_of_twin_elements.insert(middle_of_list, "-"+str(moves)+"a")
        sequence_of_twin_elements.insert(middle_of_list, "-"+str(moves)+"a")

    if not sequence_of_twin_elements:
        print(f"You have won in {moves} turns!")
        break
    moves += 1
    command = input()

if sequence_of_twin_elements:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_twin_elements))
