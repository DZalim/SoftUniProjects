from collections import deque

green_light_second = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0
crash = False

command = input()
while command != "END":
    if command != "green":
        cars.append(command)
    elif command == "green":
        time_to_pass = green_light_second
        for car in cars.copy():
            if time_to_pass > 0:
                cars.popleft()
            else:
                continue

            if time_to_pass + free_window < len(car):
                print("A crash happened!")
                letter_index = time_to_pass + free_window
                character_hit = car[letter_index]
                print(f"{car} was hit at {character_hit}.")
                crash = True
                break
            time_to_pass -= len(car)
            passed_cars += 1

    if crash:
        break
    command = input()

else:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
    