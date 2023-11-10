text_with_emoticons = input()

for index in range(len(text_with_emoticons)):
    if text_with_emoticons[index] == ":":
        print(f"{text_with_emoticons[index]}{text_with_emoticons[index + 1]}")
