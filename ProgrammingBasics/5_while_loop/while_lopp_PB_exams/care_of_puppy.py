kg_of_food = int(input())
gr_of_food = kg_of_food * 1000

needed_food = 0

command = input()
while command != "Adopted":
    gr_of_eaten_food = int(command)
    needed_food += gr_of_eaten_food
    command = input()

diff = abs(gr_of_food - needed_food)

if gr_of_food >= needed_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
