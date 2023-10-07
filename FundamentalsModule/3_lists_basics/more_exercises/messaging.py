indexes_in_str = input().split()
encrypted_message = input()

indexes_in_int = []
sum_of_indexes_in_int = []
decrypted_message = []

for integer in indexes_in_str:
    indexes_in_int.append(int(integer))

for element in indexes_in_int:
    sum_of_element = 0
    for digit in str(element):
        sum_of_element += int(digit)
    sum_of_indexes_in_int.append(sum_of_element)

index = 0
while len(decrypted_message) < len(sum_of_indexes_in_int):
    if sum_of_indexes_in_int[index] >= len(encrypted_message):
        index_for_append = sum_of_indexes_in_int[index]-len(encrypted_message)
        decrypted_message.append(encrypted_message[index_for_append])
    else:
        index_for_append = sum_of_indexes_in_int[index]
        decrypted_message.append(encrypted_message[index_for_append])

    encrypted_message_last = encrypted_message.replace(encrypted_message[index_for_append], "", 1)
    encrypted_message = encrypted_message_last
    index += 1

print("".join(decrypted_message))


