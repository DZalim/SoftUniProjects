command = input()

my_dict_force_side_users = {}

while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_user_in_values = False
        for list_of_values in my_dict_force_side_users.values():
            for value in list_of_values:
                if value == force_user:
                    force_user_in_values = True
                    break
        if force_side not in my_dict_force_side_users.keys() and not force_user_in_values:
            my_dict_force_side_users[force_side] = [force_user]
        elif force_side in my_dict_force_side_users.keys() and not force_user_in_values:
            my_dict_force_side_users[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        user_in_dictionary = False
        if force_side in my_dict_force_side_users.keys():
            for side, users in my_dict_force_side_users.items():
                if force_user in users:
                    user_in_dictionary = True
                    for user in users:
                        if side != force_side and user == force_user:
                            my_dict_force_side_users[side].remove(user)
                            my_dict_force_side_users[force_side].append(force_user)
                            print(f"{force_user} joins the {force_side} side!")
                if user_in_dictionary:
                    break
            if not user_in_dictionary:
                my_dict_force_side_users[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
        if force_side not in my_dict_force_side_users.keys() and not user_in_dictionary:
            my_dict_force_side_users[force_side] = [force_user]
            print(f"{force_user} joins the {force_side} side!")
    command = input()

for side, users in my_dict_force_side_users.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
