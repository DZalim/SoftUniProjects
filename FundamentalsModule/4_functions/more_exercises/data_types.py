def calculate_data_types(text, command):
    if text == "int":
        return int(command) * 2
    elif text == "real":
        result = int(command) * 1.5
        return f"{result:.2f}"
    elif text == "string":
        return f"${command}$"


type_of_text = input()
action = input()
final_result = calculate_data_types(type_of_text, action)
print(final_result)