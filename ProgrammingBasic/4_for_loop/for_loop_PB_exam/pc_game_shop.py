number_of_saled_games = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for game in range (number_of_saled_games):
    name_of_game = input()
    if name_of_game == "Hearthstone":
        hearthstone += 1
    elif name_of_game == "Fornite":
        fornite += 1
    elif name_of_game == "Overwatch":
        overwatch += 1
    else:
        others += 1

percent_hearthstone = hearthstone / number_of_saled_games * 100
percent_fornite = fornite / number_of_saled_games * 100
percent_overwatch = overwatch / number_of_saled_games * 100
percent_others = others / number_of_saled_games * 100

print(f"Hearthstone - {percent_hearthstone:.2f}%")
print(f"Fornite - {percent_fornite:.2f}%")
print(f"Overwatch - {percent_overwatch:.2f}%")
print(f"Others - {percent_others:.2f}%")
