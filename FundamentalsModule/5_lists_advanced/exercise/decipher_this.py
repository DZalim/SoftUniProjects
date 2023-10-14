secret_message = input().split()

loop_counter = 0
for word in secret_message:
    number = int("".join([number for number in word if number.isdigit()]))
    string = [letter for letter in word if not letter.isdigit()]
    decipher_number = chr(number)
    string[0], string[-1] = string[-1], string[-0]
    secret_message[loop_counter] = decipher_number + "".join(string)
    loop_counter += 1

print(" ".join(secret_message))
