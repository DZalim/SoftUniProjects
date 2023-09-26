name_of_tournaments = input()

win_games = 0
lost_games = 0
total_games = 0

while name_of_tournaments != "End of tournaments":
    number_of_tournaments = int(input())
    for tournament in range (1, number_of_tournaments +1):
        points_team_Desi = int(input())
        points_other_team = int(input())
        total_games += 1
        diff = abs(points_other_team - points_team_Desi)
        if points_team_Desi > points_other_team:
            win_games += 1
            print(f"Game {tournament} of tournament {name_of_tournaments}: win with {diff} points.")
        else:
            lost_games += 1
            print(f"Game {tournament} of tournament {name_of_tournaments}: lost with {diff} points.")
    name_of_tournaments = input()

percent_win_games = win_games / total_games * 100
percent_lost_games = lost_games / total_games * 100

print(f"{percent_win_games:.2f}% matches win")
print(f"{percent_lost_games:.2f}% matches lost")