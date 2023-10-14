first_sequences_of_strings = input().split(", ")
second_sequences_of_strings = input().split(", ")

filtered_result = []

for first_string in first_sequences_of_strings:
    for second_string in second_sequences_of_strings:
        if first_string in second_string:
            filtered_result.append(first_string)
            break

print(filtered_result)