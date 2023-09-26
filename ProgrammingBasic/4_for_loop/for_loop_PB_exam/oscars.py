name_of_actor = input()
academy_points = float(input())
number_of_jurys = int(input())

points = academy_points

for jury in range (number_of_jurys):
    name_of_jury = input()
    jury_points = float(input())
    points += len(name_of_jury) * jury_points / 2
    if points > 1250.5:
        break

diff = 1250.5 - points

if points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
