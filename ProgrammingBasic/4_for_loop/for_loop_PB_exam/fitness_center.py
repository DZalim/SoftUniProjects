number_of_visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

for visitor in range(number_of_visitors):
    fitness = input()
    if fitness == "Back":
        back += 1
    elif fitness == "Chest":
        chest += 1
    elif fitness == "Legs":
        legs += 1
    elif fitness == "Abs":
        abs += 1
    elif fitness == "Protein shake":
        protein_shake += 1
    elif fitness == "Protein bar":
        protein_bar +=1

total_training = back + chest + legs + abs
total_protein = protein_bar + protein_shake
percent_training = total_training / number_of_visitors * 100
percent_protein = total_protein / number_of_visitors * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{percent_training:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")

