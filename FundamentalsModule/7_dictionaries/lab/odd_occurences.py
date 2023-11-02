list_of_words = input().lower().split()

my_dict = dict.fromkeys(list_of_words, 0)

for word in list_of_words:
    if word in my_dict:
        my_dict[word] += 1

for key, value in my_dict.items():
    if value % 2 != 0:
        print(f"{key}", end=" ")
