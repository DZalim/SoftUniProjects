number_of_electrons = int(input())

all_shells = []

for shell in range(1, number_of_electrons+1):
    max_number_of_current_shell = 2*shell**2
    if max_number_of_current_shell <= number_of_electrons:
        all_shells.append(max_number_of_current_shell)
    else:
        all_shells.append(number_of_electrons)
    number_of_electrons -= max_number_of_current_shell
    if number_of_electrons <= 0:
        break

print(all_shells)
