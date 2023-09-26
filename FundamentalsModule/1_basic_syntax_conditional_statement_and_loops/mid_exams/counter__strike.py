initial_energy = int(input())

battle = 0

while True:
    command = input()
    if command == "End of battle":
        print(f"Won battles: {battle}. Energy left: {initial_energy}")
        break
    distance = int(command)
    if distance > initial_energy:
        print(f"Not enough energy! Game ends with {battle} won battles and {initial_energy} energy")
        break
    initial_energy -= distance
    battle += 1
    if battle % 3 == 0:
        initial_energy += battle


