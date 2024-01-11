current_string_as_list = [char for char in input()]
stack = []

while current_string_as_list:
    stack.append(current_string_as_list.pop())

print("".join(stack))
