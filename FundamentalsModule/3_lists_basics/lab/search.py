n = int(input())
needed_word = input()

all_list = []
needed_list = []

for word in range (n):
    current_word = input()
    all_list.append(current_word)
    if needed_word in current_word:
        needed_list.append(current_word)

print(all_list)
print(needed_list)