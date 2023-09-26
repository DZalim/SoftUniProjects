name_of_actor = input()
academy_points = float(input())
number_of_jurys = int(input())

total_points = academy_points

for actor in range (number_of_jurys):
    name_of_jury = input()
    jury_points = float(input())
    total_points += len(name_of_jury) * jury_points / 2
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")