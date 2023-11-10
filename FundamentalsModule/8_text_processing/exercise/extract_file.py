path_to_a_file = input().split("\\")

last_index = path_to_a_file[-1]
filename, extension = last_index.split(".")

print(f"File name: {filename}")
print(f"File extension: {extension}")
