import os

file_name = 'numbers.txt'
file_path = os.path.join('resources', file_name)

file = open(file_path)
lines = file.readlines()
file.close()

total_sum = 0

for line in lines:
    total_sum += int(line.strip())

print(total_sum)
