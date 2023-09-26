import math

number_of_easter_breads = int(input())

kg_sugar = 0
kg_flour = 0
max_sugar = 0
max_flour = 0

for easter_bread in range(number_of_easter_breads):
    sugar = int(input())
    flour = int(input())
    kg_flour += flour
    kg_sugar += sugar
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

packet_sugar = math.ceil(kg_sugar / 950)
packet_flour = math.ceil(kg_flour / 750)

print(f"Sugar: {packet_sugar}")
print(f"Flour: {packet_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
