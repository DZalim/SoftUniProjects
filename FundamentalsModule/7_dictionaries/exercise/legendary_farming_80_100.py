key_materials = ["shards", "fragments", "motes"]
legendary_win = {"Shadowmourne": key_materials[0], "Valanyr": key_materials[1], "Dragonwrath": key_materials[2]}

legendary_item_is_find = False

dict_of_items = dict.fromkeys(key_materials, 0)

while True:
    legendary_items = input().split()
    for index in range(1, len(legendary_items), 2):
        material = legendary_items[index].lower()
        quantity = int(legendary_items[index-1])
        if material not in dict_of_items:
            dict_of_items[material] = 0
        dict_of_items[material] += quantity
        for key, value in dict_of_items.items():
            if value >= 250:
                legendary_item_is_find = True
                dict_of_items[key] -= 250
                for legendary, item in legendary_win.items():
                    if key == item:
                        print(f"{legendary} obtained!")
                        break
            if legendary_item_is_find:
                break
        if legendary_item_is_find:
            break
    if legendary_item_is_find:
        break

for material, quantity in dict_of_items.items():
    print(f"{material}: {quantity}")
