text = input()

sums = 0

for letter in text:
    if letter == "a":
        sums += 1
    if letter == "e":
        sums += 2
    if letter == "i":
        sums += 3
    if letter == "o":
        sums += 4
    if letter == "u":
        sums += 5

print(sums)