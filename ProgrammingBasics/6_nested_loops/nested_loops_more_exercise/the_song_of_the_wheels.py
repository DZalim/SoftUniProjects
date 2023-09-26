control_value = int(input())

counter = 0
fourth_combinations = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if control_value == a * b + c * d and a < b and c > d:
                    counter += 1
                    print(f"{a}{b}{c}{d}", end=" ")
                    if counter == 4:
                        fourth_combinations = True
                        combination = str(a)+str(b)+str(c)+str(d)
print()
if fourth_combinations:
    print(f"Password: {combination}")
else:
    print("No!")
