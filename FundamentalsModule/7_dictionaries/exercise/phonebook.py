data = input()

my_phonebook = {}

while "-" in data:
    name, number = data.split("-")
    my_phonebook[name] = number
    data = input()

number_n = int(data)

searched_people = []

for searched_names in range(number_n):
    searched_name = input()
    searched_people.append(searched_name)

for people in searched_people:
    if people in my_phonebook:
        print(f"{people} -> {my_phonebook[people]}")
    else:
        print(f"Contact {people} does not exist.")
