name_of_football_team = input()
number_of_match = int(input())

w = 0
d = 0
l = 0
points = 0

for match in range(number_of_match):
    result = input()
    if result == "W":
        w += 1
        points +=3
    elif result == "D":
        d += 1
        points += 1
    elif result == "L":
        l += 1

if number_of_match == 0:
    print(f"{name_of_football_team} hasn't played any games during this season.")
else:
    win_rate = w / number_of_match * 100
    print(f"{name_of_football_team} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {w}")
    print(f"## D: {d}")
    print(f"## L: {l}")
    print(f"Win rate: {win_rate:.2f}%")
