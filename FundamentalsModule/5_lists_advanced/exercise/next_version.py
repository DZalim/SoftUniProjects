version_of_software = [int(number) for number in input().split(".")]

version_of_software[-1] += 1
for number in range(len(version_of_software)-1, -1, -1):
    if version_of_software[number] > 9:
        version_of_software[number] = 0
        if number == 0:
            break
        version_of_software[number-1] += 1

print(".".join(str(number) for number in version_of_software))



