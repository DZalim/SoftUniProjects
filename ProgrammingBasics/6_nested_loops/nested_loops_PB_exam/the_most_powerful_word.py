word = input()

most_powerful_word = ""
points_word = 0

while word != "End of words":
    point = 0
    for letter in word:
        point += ord(letter)
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" or\
            word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
        point *= len(word)
    else:
        point //= len(word)
    if point > points_word:
        points_word = point
        most_powerful_word = word
    word = input()

print(f"The most powerful word is {most_powerful_word} - {points_word}")