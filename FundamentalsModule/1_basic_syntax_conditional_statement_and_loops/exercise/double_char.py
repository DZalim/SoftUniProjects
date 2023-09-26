word = input()

while word != "End":
    double_char = ""
    if word == "SoftUni":
        word = input()
        continue
    else:
        for current_word in range (len(word)):
            double_char += word[current_word] * 2
        print(double_char)
    word = input()