journal_with_collection = [collection for collection in input().split(", ")]

command = input()
while command != "Craft!":
    split_command = command.split(" - ")
    action = split_command[0]
    item = split_command[1]
    if action == "Collect":
        if item not in journal_with_collection:
            journal_with_collection.append(item)
    elif action == "Drop":
        if item in journal_with_collection:
            journal_with_collection.remove(item)
    elif action == "Combine Items":
        split_item = item.split(":")
        old_item = split_item[0]
        new_item = split_item[1]
        if old_item in journal_with_collection:
            old_item_index = journal_with_collection.index(old_item)
            journal_with_collection.insert(old_item_index+1, new_item)
    elif action == "Renew":
        if item in journal_with_collection:
            journal_with_collection.append(item)
            journal_with_collection.remove(item)
    command = input()

print(", ".join(journal_with_collection))
