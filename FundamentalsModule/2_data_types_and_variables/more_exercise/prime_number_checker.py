number_for_check = int(input())

number_is_prime = True

for delimiter in range (2, number_for_check):
    if number_for_check % delimiter == 0:
        number_is_prime = False
        print(f"False")
        break

if number_is_prime:
    print(f"True")