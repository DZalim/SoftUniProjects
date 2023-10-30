people_waiting_lift = int(input())
empty_places_in_lift_in_str = input().split()

places_in_lift = []

for empty_places in empty_places_in_lift_in_str:
    if people_waiting_lift > 4:
        peoples = 4 - int(empty_places)
    else:
        peoples = people_waiting_lift
    places_in_lift.append(str(int(peoples + int(empty_places))))
    people_waiting_lift -= peoples

if int(places_in_lift[-1]) < 4:
    print("The lift has empty spots!")
elif people_waiting_lift > 0:
    print(f"There isn't enough space! {people_waiting_lift} people in a queue!")

print(" ".join(places_in_lift))
