class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        to_return = ""
        if species == "mammal":
            to_return += f"Mammals in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            to_return += f"Fishes in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            to_return += f"Birds in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"
        return to_return


name_of_the_zoo = input()
total_rows = int(input())
zoo_object = Zoo(name_of_the_zoo)

for animal in range(total_rows):
    command = input()
    species, name = command.split()
    zoo_object.add_animal(species, name)

species = input()
print(zoo_object.get_info(species))
