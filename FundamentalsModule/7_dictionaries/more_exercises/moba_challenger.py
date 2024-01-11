command = input()

my_dict_with_player_position_and_skills = {}

while command != "Season end":
    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in my_dict_with_player_position_and_skills.keys():
            my_dict_with_player_position_and_skills[player] = {position: skill}
        else:
            if position not in my_dict_with_player_position_and_skills[player].keys():
                my_dict_with_player_position_and_skills[player][position] = skill
            else:
                if my_dict_with_player_position_and_skills[player][position] < skill:
                    my_dict_with_player_position_and_skills[player][position] = skill
    elif " vs " in command:
        player_one, player_two = command.split(" vs ")
        if player_one in my_dict_with_player_position_and_skills.keys() and player_two in my_dict_with_player_position_and_skills.keys():
            for first_player_values in my_dict_with_player_position_and_skills.values():
                for second_player_values in my_dict_with_player_position_and_skills.values():
                    if first_player_values.keys() == second_player_values.keys():
                        if first_player_values.values() > second_player_values.values():
                            pass
    command = input()

print(my_dict_with_player_position_and_skills)
