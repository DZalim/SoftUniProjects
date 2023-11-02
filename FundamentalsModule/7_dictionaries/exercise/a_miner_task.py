command = input()

my_dict = {}

while command != "stop":
    key = command
    value = int(input())
    if key not in my_dict:
        my_dict[key] = 0
    my_dict[key] += value
    command = input()

for key, value in my_dict.items():
    print(f"{key} -> {value}")
