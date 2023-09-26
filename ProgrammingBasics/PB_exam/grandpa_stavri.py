number_of_days = int(input())

total_litres = 0
total_degree = 0

for day in range(1, number_of_days + 1):
    quantity_of_raki = float(input())
    degree_of_drink = float(input())
    degree_for_quantity = quantity_of_raki * degree_of_drink
    total_litres += quantity_of_raki
    total_degree += degree_for_quantity

average_degree = total_degree / total_litres

print(f"Liter: {total_litres:.2f}")
print(f"Degrees: {average_degree:.2f}")

if average_degree < 38:
    print("Not good, you should baking!")
elif average_degree > 42:
    print("Dilution with distilled water!")
else:
    print("Super!")
