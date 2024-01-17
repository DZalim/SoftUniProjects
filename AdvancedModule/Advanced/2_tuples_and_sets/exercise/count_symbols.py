text = tuple(input())

for letter in sorted(set(text)):
    print(f'{letter}: {text.count(letter)} time/s')
