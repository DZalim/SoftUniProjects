from collections import deque

boxes_with_materials = [int(x) for x in input().split()]  # stack
magic_level = deque(int(x) for x in input().split())  # queue

needed_magic = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

craft_presents = []

while boxes_with_materials and magic_level:
    last_material = boxes_with_materials.pop()
    first_magic = magic_level.popleft()

    result = last_material * first_magic

    if result == 0:
        if last_material > 0 and first_magic == 0:
            boxes_with_materials.append(last_material)
        if first_magic > 0 and last_material == 0:
            magic_level.appendleft(first_magic)
        continue

    if result in needed_magic.keys():
        craft_presents.append(needed_magic[result])
    elif result < 0:
        result = last_material + first_magic
        boxes_with_materials.append(result)
    else:
        boxes_with_materials.append(last_material + 15)

set1 = {'Doll', 'Wooden train'}
set2 = {'Teddy bear', 'Bicycle'}

if set1.issubset(craft_presents) or set2.issubset(craft_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes_with_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(boxes_with_materials))}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for present in sorted(set(craft_presents)):
    print(f"{present}: {craft_presents.count(present)}")
