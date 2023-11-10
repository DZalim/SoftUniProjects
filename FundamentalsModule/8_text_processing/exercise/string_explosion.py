text = input()

explosion_count = 0
new_text = ""

for index in range(len(text)):
    if explosion_count == 0 or text[index] == ">":
        if text[index] == ">":
            explosion_count += int(text[index+1])
        new_text += text[index]
    else:
        explosion_count -= 1

print(new_text)
