sum_for_beggars = input().split(", ")
count_of_beggars = int(input())

sum_for_each_beggar = []

for beggar in range(count_of_beggars):
    sum_for_beggar = 0
    for current_sum in range(beggar, len(sum_for_beggars), count_of_beggars):
        sum_for_beggar += int(sum_for_beggars[current_sum])
    sum_for_each_beggar.append(sum_for_beggar)

print(sum_for_each_beggar)

