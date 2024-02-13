from collections import deque

elfs_energy = deque(int(x) for x in input().split()) #queue
number_of_materials_in_a_box = [int(x) for x in input().split()] #stack

toys = 0
total_used_energy = 0
rotation = 1

while elfs_energy and number_of_materials_in_a_box:
    first_elf_energy = elfs_energy.popleft()

    if first_elf_energy >= 5:
        last_material = number_of_materials_in_a_box[-1]

        if rotation % 3 == 0:
            last_material *= 2

        if first_elf_energy >= last_material:
            number_of_materials_in_a_box.pop()
            made_toy = 2 if rotation % 3 == 0 else 1
            total_used_energy += last_material
            left_energy = first_elf_energy - last_material + 1
            elfs_energy.append(left_energy)

            if rotation % 5 == 0:
                elfs_energy[-1] -= 1
                continue

            toys += made_toy

        else:
            elfs_energy.append(first_elf_energy * 2)

        rotation += 1

print(f"Toys: {toys}")
print(f"Energy: {total_used_energy}")
if elfs_energy:
    print(f"Elves left: {', '.join(str(x) for x in elfs_energy)}")
if number_of_materials_in_a_box:
    print(f"Boxes left: {', '.join(str(x) for x in number_of_materials_in_a_box)}")
