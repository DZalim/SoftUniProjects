number_of_commands = int(input())

my_dict_with_registers = {}

for command in range(number_of_commands):
    current_command = input().split()
    action = current_command[0]
    if action == "register":
        name_for_register, current_register = current_command[1], current_command[2]
        if name_for_register not in my_dict_with_registers.keys():
            my_dict_with_registers[name_for_register] = current_register
            print(f"{name_for_register} registered {current_register} successfully")
        else:
            print(f"ERROR: already registered with plate number {current_register}")
    elif action == "unregister":
        name_for_unregister = current_command[1]
        if name_for_unregister not in my_dict_with_registers.keys():
            print(f"ERROR: user {name_for_unregister} not found")
        else:
            print(f"{name_for_unregister} unregistered successfully")
            del my_dict_with_registers[name_for_unregister]

for username, license_plate_number in my_dict_with_registers.items():
    print(f"{username} => {license_plate_number}")
