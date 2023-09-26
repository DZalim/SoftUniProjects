max_goals = 0
best_player = ""
is_hat_trick = False

name_of_player = input()
while name_of_player != "END":
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = name_of_player
    if goals >= 3:
        is_hat_trick = True
    if goals >= 10:
        break
    name_of_player = input()

print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")