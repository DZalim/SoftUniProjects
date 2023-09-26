name_of_player = input()

max_points = 0
winner = ""

while name_of_player != "Stop":
    points = 0
    for letter in name_of_player:
        number = int(input())
        if ord(letter) == number:
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points = points
        winner = name_of_player
    name_of_player = input()

print(f"The winner is {winner} with {max_points} points!")