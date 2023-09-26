number_of_tournament = int(input())
start_points = int(input())

points = 0
won = 0

for tournament in range (number_of_tournament):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        points += 2000
        won += 1
    elif stage_of_tournament == "F":
        points += 1200
    elif stage_of_tournament == "SF":
        points += 720

average_points = points // number_of_tournament
points += start_points
percent_won = won / number_of_tournament * 100

print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{percent_won:.2f}%")


