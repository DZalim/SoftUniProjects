number_of_tournaments = int(input())
start_points = float(input())

points = 0
w = 0

for match in range (number_of_tournaments):
    stage = input()
    if stage == "W":
        points += 2000
        w += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

average_points = points // number_of_tournaments
points += start_points
win_rate = w / number_of_tournaments * 100

print(f"Final points: {int(points)}")
print(f"Average points: {average_points}")
print(f"{win_rate:.2f}%")
